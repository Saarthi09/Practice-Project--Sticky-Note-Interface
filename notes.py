import json

notes = []
count = 0

while True:
    count += 1

    note_title = input("Title your note (leave blank if none): ")
    note_text = input("Write a note: ")

    if note_text == "":
        break

    if note_title == "":
        note_title = str(count)

    notes.append({
        "title": note_title,
        "text": note_text
    })

with open("notes.json", "w") as file:
    json.dump(notes, file, indent=4)
print("Saved")