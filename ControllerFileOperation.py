import Note

FILE_NAME = 'notes.csv'


def write_file(data, mode='a'):
    with (open(FILE_NAME, mode, encoding="utf-8")) as _file:
        for notes in data:
            _file.write(Note.Note.to_string(notes) + '\n')


def read_file():
    data = []
    with (open(FILE_NAME, 'r', encoding="utf-8")) as _file:
        notes = _file.read().strip().split("\n")
        for line in notes:
            note_parts = line.split(';')
            note = Note.Note(
                id=note_parts[0],
                title=note_parts[1],
                body=note_parts[2],
                date=note_parts[3]
            )
            data.append(note)
    return data
