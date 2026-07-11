import tkinter as tk

root = tk.Tk()
root.title("Sticky notes")
root.geometry("600x600")
root.configure(bg="khaki")

note_count = 0

label = tk.Label(
    root,
    text="Sticky notes",
    font=("Times New Roman", 20),
    bg="Yellow"
)
label.place(x=250, y=50)

def done(button):
    button.config(text="Saved!")

    button.after(2000, lambda: button.config(text="Save"))

def create_note(colour):
    global note_count
    note_count += 1

    new_window = tk.Toplevel(root)
    new_window.title(f"Note {note_count}")
    new_window.geometry("400x400")
    new_window.configure(bg=colour)

    text_box = tk.Text(new_window, width=40, height=10, wrap="word", bg=colour)
    text_box.pack(pady=20)

    save_btn = tk.Button(
        new_window,
        text="Save",
        font=("Times New Roman", 10),
        bg="khaki",
        command=lambda: done(save_btn)
    )
    save_btn.place(x=300, y=300)

    note_btn = tk.Button(
        root,
        text=f"Note {note_count}",
        command=new_window.lift
    )

    note_btn.place(x=300, y=100 + 40 * note_count)

def colour_picker():
    colour_options = tk.Toplevel(root)
    colour_options.geometry("200x200")
    colour_options.configure(bg="coral")
    colour_options.title("Colour Picker")

    label = tk.Label(colour_options, text="Choose a colour", bg= "skyblue", font=("Times New Roman", 10))
    label.pack()

    red_button = tk.Button(colour_options, bg="red", width=2, height=1, command=lambda: [create_note("red"), colour_options.destroy()])
    red_button.pack()
    red_button.place(x=10, y=50)

    blue_button = tk.Button(colour_options, bg="skyblue", width=2, height=1, command=lambda: [create_note("skyblue"), colour_options.destroy()])
    blue_button.pack()
    blue_button.place(x=50, y=50)

    yellow_button = tk.Button(colour_options, bg="yellow", width=2, height=1, command= lambda: [create_note("yellow"), colour_options.destroy()])
    yellow_button.pack()
    yellow_button.place(x=90, y=50)

    green_button = tk.Button(colour_options, bg="lightgreen", width=2, height=1, command= lambda: [create_note("lightgreen"), colour_options.destroy()])
    green_button.pack()
    green_button.place(x=130, y=50)

    pink_button = tk.Button(colour_options, bg="pink", width=2, height=1, command= lambda: [create_note("pink"), colour_options.destroy()])
    pink_button.pack()
    pink_button.place(x=170, y=50)

create_btn = tk.Button(
    root,
    text="Create Note",
    font=("Times New Roman", 14),
    bg="khaki",
    command=colour_picker)
create_btn.place(x=100, y=150)


exit_btn = tk.Button(
    root,
    text="Exit",
    font=("Times New Roman", 14),
    command=root.destroy
)
exit_btn.place(x=100, y=200)







root.mainloop()