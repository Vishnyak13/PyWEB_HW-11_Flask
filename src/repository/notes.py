from src import models, db
import datetime


def create_notes(title, text, tags):
    tags_obj = []
    for tag in tags:
        tags_obj.append(db.session.query(models.Tag).filter(models.Tag.name == tag).first())
    note = models.Note(title=title, text=text, tags=tags_obj)
    db.session.add(note)
    db.session.commit()


def update_notes(note_id, title, text, tags):
    tags_obj = []
    for tag in tags:
        tags_obj.append(db.session.query(models.Tag).filter(models.Tag.name == tag).first())
    note = models.Note.query.filter_by(id=note_id).first()
    note.title = title
    note.text = text
    note.tags = tags_obj
    db.session.commit()


def delete_notes(note_id):
    db.session.query(models.Note).filter(models.Note.id == note_id).delete()
    db.session.commit()


def get_note_by_id(note_id):
    note = models.Note.query.filter_by(id=note_id).first()
    return note


def get_notes_by_tag(tag):
    notes = models.Note.query.filter_by(tag=tag).all()
    return notes


def get_all_notes():
    notes = models.Note.query.all()
    return notes


def add_tag(name):
    tag = models.Tag(name=name)
    db.session.add(tag)
    db.session.commit()


def get_all_tags():
    tags = models.Tag.query.all()
    return tags
