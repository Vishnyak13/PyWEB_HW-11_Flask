from src import models, db
import datetime


def create_notes(title, note_text, tags):
    note = models.Note(title=title, note_text=note_text, created_at=datetime.datetime.now())
    for tag in tags:
        tag = models.Tag.query.filter_by(tag_name=tag).first()
        note.tags.append(tag)
    db.session.add(note)
    db.session.commit()


def update_notes(title, note_text, tags):
    note = models.Note.query.filter_by(title=title).first()
    note.note_text = note_text
    for tag in tags:
        tag = models.Tag.query.filter_by(tag_name=tag).first()
        note.tags.append(tag)
    db.session.commit()


def delete_notes(title):
    note = models.Note.query.filter_by(title=title).first()
    db.session.delete(note)
    db.session.commit()


def get_note_by_title(title):
    note = models.Note.query.filter_by(title=title).first()
    return note


def get_notes_by_tag(tag):
    notes = models.Note.query.filter_by(tag=tag).all()
    return notes


def get_all_notes():
    notes = models.Note.query.all()
    return notes


def add_tag_to_note(title, tag):
    note = models.Note.query.filter_by(title=title).first()
    tag = models.Tag.query.filter_by(tag_name=tag).first()
    note.tags.append(tag)
    db.session.commit()
