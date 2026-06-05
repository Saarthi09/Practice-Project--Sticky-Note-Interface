import json
import os
if os.path.exists("notes.json"):
    with open("notes.json", "r") as file:
        notes = json.load(file)
else:
    notes = []
count = len(notes)

while True:
    count += 1

    note_title = input("Title your note (leave blank if none): ")
    note_text = input("Write a note (leave blank to quit): ")

    if note_text == "":
        break

    if note_title == "":
        note_title = "note " + str(count)

    notes.append({
        "title": note_title,
        "text": note_text
    })

    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)
    print("Saved")

    if input("Add another note?(y/n)").lower() != "y":
        break