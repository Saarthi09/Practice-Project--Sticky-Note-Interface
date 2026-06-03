import json

notes = []
while True:
    note_text = input("Write a note (or 'done'): ")

    if note_text == "done":
        break

    notes.append(
        {
        "text": note_text
        })
with open("notes.json", "w") as file:
    json.dump(notes, file, indent=4)