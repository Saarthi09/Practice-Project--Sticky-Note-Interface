import tkinter as tk


class StickyNote:
    def __init__(self, app, colour):
        self.app = app
        self.number = app.note_count
        self.colour = colour

        self.window = tk.Toplevel(app.root)
        self.window.title(f"Note {self.number}")
        self.window.geometry("400x400") 
        self.window.configure(bg=self.colour)

        self.text_box = tk.Text(
            self.window,
            width=40,
            height=10,
            wrap="word",
            bg=self.colour
        )
        self.text_box.pack(pady=20)

        self.save_btn = tk.Button(
            self.window,
            text="Save",
            font=("Times New Roman", 10),
            bg="khaki",
            command=self.done
        )
        self.save_btn.place(x=300, y=300)

        self.note_btn = tk.Button(
            app.root,
            text=f"Note {self.number}",
            command=self.window.lift
        )
        self.note_btn.place(x=300, y=100 + 40 * self.number)

    def done(self):
        self.save_btn.config(text="Saved!")
        self.save_btn.after(
            2000,
            lambda: self.save_btn.config(text="Save")
        )


class NotesApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sticky notes")
        self.root.geometry("600x600")
        self.root.configure(bg="khaki")

        self.note_count = 0
        self.notes = []

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
            command=self.root.destroy
        )
        self.exit_btn.place(x=100, y=200)

    def create_note(self, colour):
        self.note_count += 1

        note = StickyNote(self, colour)
        self.notes.append(note)

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

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = NotesApp()
    app.run()