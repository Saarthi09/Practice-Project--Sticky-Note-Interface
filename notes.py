import json
import os

from notes_functions import (
    add_note,
    view_notes,
    edit_note,
    delete_note,
)

if os.path.exists("notes.json"):
    with open("notes.json", "r") as file:
        notes = json.load(file)
else:
    notes = []

while True:
    print("""
========= NOTES APP =========

1. Add Note
2. View Notes
3. Edit Note
4. Delete Note
5. Exit

=============================
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_note(notes)

    elif choice == "2":
        view_notes(notes)

    elif choice == "3":
        edit_note(notes)

    elif choice == "4":
        delete_note(notes)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")