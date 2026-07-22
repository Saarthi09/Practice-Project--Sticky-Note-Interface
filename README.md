# Sticky Notes

A desktop sticky notes application built with Python and Tkinter.

The application allows users to create, edit, save, reopen, and delete color-coded sticky notes. Notes are automatically stored locally in JSON format, allowing them to persist between sessions.

## Features

- Create unlimited sticky notes
- Choose from multiple note colors
- Edit notes at any time
- Save notes locally
- Reopen previously created notes
- Delete notes permanently
- Scrollable notes list
- Automatic persistence between sessions

## Tech Stack

- Python
- Tkinter
- JSON

## Project Structure

```
.
├── sticky_notes.py          # Main application
├── sticky_notes_data.json   # Saved notes (generated automatically)
└── README.md
```

## Run

```bash
python sticky_notes.py
```

No external libraries are required. Tkinter is included with the standard Python installation.

## How It Works

- Click **Create Note**.
- Select a note color.
- Write your note.
- Press **Save** to store it.
- Closing a note hides it instead of deleting it.
- Reopen notes from the **Your Notes** list.
- Delete removes the note from both the application and local storage.

## Data Storage

Notes are stored in `sticky_notes_data.json` in the following format:

```json
{
    "1": {
        "colour": "yellow",
        "text": "Finish assignment"
    },
    "2": {
        "colour": "skyblue",
        "text": "Buy groceries"
    }
}
```

## Screenshots

Screenshots can be added here.

## Future Improvements

- Search notes
- Pin important notes
- Dark mode
- Custom colors
- Rich text formatting
- Reminders and notifications
