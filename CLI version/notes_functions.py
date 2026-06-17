import json
def add_note(notes):
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

        if input("Add another note? (y/n): ").lower() != "y":
            break
        
def view_notes(notes):
    if len(notes) == 0:
        print("No notes found")
        return
    for i, note in enumerate(notes, start=1):
        print(f"\n{i}. {note['title']}")
        print(note["text"])

def edit_note(notes):
    if len(notes) ==0:
        print("No notes found")
        return
    
    view_notes(notes)

    try:
        choice = int(input("Enter note number to edit: ")) -1
        
        if 0<= choice<len(notes):
            new_title = input("New title(leave bank to keep current)")
            new_text = input("New text(leave blank to keep current)")

            if new_title:
                notes[choice]["title"] = new_title
            
            if new_text:
                notes[choice]["text"] = new_text

            with open("notes.json", "w") as file:
                json.dump(notes,file,indent=4)

            print("Note updated")

        else:
            print("Invalid note number")
    except: 
        print("Please enter a valid note number")

def delete_note(notes):
    if len(notes) ==0:
        print("No notes found")
        return

    view_notes(notes)

    try:
        choice = int(input("Enter note number to delete: ")) -1

        if 0<= choice<len(notes):
            del notes[choice]
            with open("notes.json", "w") as file:
                json.dump(notes, file, indent=4)
            print(f"Note {choice +1} successfully deleted")
    except:
        print("Please enter a valid note number")