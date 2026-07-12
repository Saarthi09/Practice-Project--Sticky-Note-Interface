
        command=lambda: done(save_btn)
    )
    save_btn.place(x=300, y=300)

    note_btn = tk.Button(
        root,
        text=f"Note {note_count}",