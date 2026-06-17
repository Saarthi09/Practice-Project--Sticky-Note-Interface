import json

def view_notes(notes):
    if len(notes) == 0:
        print("No notes found")
        return
    for i, note in enumerate(notes, start=1):
        print(f"\n{i}. {note['title']}")
        print(note["text"])