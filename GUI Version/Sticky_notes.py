import tkinter as tk
import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sticky_notes_data.json")


class StickyNote:
    """A single sticky note window plus its launcher button on the main app."""

    def __init__(self, app, note_id, colour, text=""):
        self.app = app
        self.note_id = note_id
        self.colour = colour

        
        self.window = tk.Toplevel(app.root)
        self.window.title(f"Note {self.note_id}")
        self.window.geometry("400x400")
        self.window.configure(bg=self.colour)

        
        self.window.protocol("WM_DELETE_WINDOW", self.close)

        self.text_box = tk.Text(
            self.window,
            width=40,
            height=10,
            wrap="word",
            bg=self.colour
        )
        self.text_box.pack(pady=20)
        if text:
            self.text_box.insert("1.0", text)

        self.save_btn = tk.Button(
            self.window,
            text="Save",
            font=("Times New Roman", 10),
            bg="khaki",
            command=self.save
        )
        self.save_btn.place(x=260, y=300)

        self.delete_btn = tk.Button(
            self.window,
            text="Delete",
            font=("Times New Roman", 10),
            bg="salmon",
            command=self.delete
        )
        self.delete_btn.place(x=320, y=300)

        
        self.note_btn = tk.Button(
            app.notes_list_inner,
            text=f"Note {self.note_id}",
            bg=self.colour,
            command=self.reopen
        )
        self.note_btn.pack(pady=2, fill="x", padx=2)

    def get_text(self):
        return self.text_box.get("1.0", "end-1c")

    def save(self, flash=True):
        """Persist this note's current text to disk."""
        self.app.notes_data[str(self.note_id)] = {
            "colour": self.colour,
            "text": self.get_text()
        }
        self.app.save_all()
        if flash:
            self.save_btn.config(text="Saved!")
            self.save_btn.after(1500, lambda: self.save_btn.config(text="Save"))

    def reopen(self):
        """Bring this note's window back on screen, restoring it if it was hidden."""
        self.window.deiconify()
        self.window.lift()

    def close(self):
        """Handle the window's X button: save, then hide (not destroy) the window.

        The note stays in the list on the main window and its data stays on
        disk, so clicking its launcher button later brings it right back.
        """
        self.save(flash=False)
        self.window.withdraw()

    def delete(self):
        """Permanently remove this note (window, launcher button, and saved data)."""
        self.app.notes_data.pop(str(self.note_id), None)
        self.app.save_all()
        self.app.notes.pop(self.note_id, None)
        self.window.destroy()
        self.note_btn.destroy()


class NotesApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sticky notes")
        self.root.geometry("600x600")
        self.root.configure(bg="khaki")

        self.next_id = 1
        self.notes = {}         
        self.notes_data = {}    

        self.label = tk.Label(
            self.root,
            text="Sticky Notes",
            font=("Times New Roman", 20),
            bg="Yellow"
        )
        self.label.place(x=250, y=50)

        self.create_btn = tk.Button(
            self.root,
            text="Create Note",
            font=("Times New Roman", 14),
            bg="khaki",
            command=self.colour_picker
        )
        self.create_btn.place(x=100, y=150)

        self.exit_btn = tk.Button(
            self.root,
            text="Exit",
            font=("Times New Roman", 14),
            command=self.exit_app
        )
        self.exit_btn.place(x=100, y=200)

        self.notes_label = tk.Label(
            self.root,
            text="Your Notes",
            font=("Times New Roman", 12, "bold"),
            bg="khaki"
        )
        self.notes_label.place(x=100, y=250)

        
        self.notes_canvas = tk.Canvas(self.root, bg="khaki", highlightthickness=0)
        self.notes_canvas.place(x=100, y=280, width=280, height=290)

        self.notes_scrollbar = tk.Scrollbar(
            self.root, orient="vertical", command=self.notes_canvas.yview
        )
        self.notes_scrollbar.place(x=380, y=280, height=290)
        self.notes_canvas.configure(yscrollcommand=self.notes_scrollbar.set)

        self.notes_list_inner = tk.Frame(self.notes_canvas, bg="khaki")
        self.notes_canvas.create_window((0, 0), window=self.notes_list_inner, anchor="nw")

        self.notes_list_inner.bind(
            "<Configure>",
            lambda e: self.notes_canvas.configure(scrollregion=self.notes_canvas.bbox("all"))
        )
        
        self.notes_canvas.bind(
            "<Enter>",
            lambda e: self.notes_canvas.bind_all(
                "<MouseWheel>",
                lambda ev: self.notes_canvas.yview_scroll(int(-ev.delta / 120), "units")
            )
        )
        self.notes_canvas.bind("<Leave>", lambda e: self.notes_canvas.unbind_all("<MouseWheel>"))

        self.load_all()

   

    def save_all(self):
        try:
            with open(DATA_FILE, "w") as f:
                json.dump(self.notes_data, f, indent=2)
        except OSError as e:
            print(f"Could not save notes: {e}")

    def load_all(self):
        if not os.path.exists(DATA_FILE):
            return
        try:
            with open(DATA_FILE, "r") as f:
                self.notes_data = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"Could not load notes: {e}")
            self.notes_data = {}
            return

        for id_str, info in self.notes_data.items():
            note_id = int(id_str)
            note = StickyNote(self, note_id, info.get("colour", "yellow"), info.get("text", ""))
            note.window.withdraw()  
            self.notes[note_id] = note
            self.next_id = max(self.next_id, note_id + 1)

    

    def create_note(self, colour):
        note_id = self.next_id
        self.next_id += 1

        note = StickyNote(self, note_id, colour)
        self.notes[note_id] = note

       
        self.notes_data[str(note_id)] = {"colour": colour, "text": ""}
        self.save_all()

    def colour_picker(self):
        colour_options = tk.Toplevel(self.root)
        colour_options.geometry("200x200")
        colour_options.configure(bg="coral")
        colour_options.title("Colour Picker")

        label = tk.Label(
            colour_options,
            text="Choose a colour",
            bg="skyblue",
            font=("Times New Roman", 10)
        )
        label.pack()

        colours = [
            ("red", 10),
            ("skyblue", 50),
            ("yellow", 90),
            ("lightgreen", 130),
            ("pink", 170)
        ]

        for colour, x in colours:
            btn = tk.Button(
                colour_options,
                bg=colour,
                width=2,
                height=1,
                command=lambda c=colour: (
                    self.create_note(c),
                    colour_options.destroy()
                )
            )
            btn.place(x=x, y=50)

    def exit_app(self):
       
        for note in list(self.notes.values()):
            note.save(flash=False)
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = NotesApp()
    app.run()
