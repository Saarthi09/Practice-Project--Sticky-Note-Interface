import json

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

        