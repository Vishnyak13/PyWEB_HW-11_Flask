from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from src import db
from src.libs.constants import CONTACT_DEFAULT_LENGTH, CONTACT_PHONE_LENGTH, CONTACT_ADDRESS_LENGTH, \
    NOTE_DEFAULT_LENGTH, NOTE_TEXT_LENGTH, TAG_NAME_LENGTH

note_m2m_tag = db.Table(
    "note_m2m_tag",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("note", db.Integer, ForeignKey("notes.id", ondelete="CASCADE")),
    db.Column("tag", db.Integer, ForeignKey("tags.id", ondelete="CASCADE")))


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(CONTACT_DEFAULT_LENGTH), nullable=False)
    last_name = db.Column(db.String(CONTACT_DEFAULT_LENGTH), nullable=False)
    email = db.Column(db.String(CONTACT_DEFAULT_LENGTH), unique=True)
    phone = db.Column(db.String(CONTACT_PHONE_LENGTH), unique=True)
    birthday = db.Column(db.DateTime)
    address = db.Column(db.String(CONTACT_ADDRESS_LENGTH))
    created = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(NOTE_DEFAULT_LENGTH), nullable=False, unique=True)
    note_text = db.Column(db.String(NOTE_TEXT_LENGTH), nullable=False)
    tags = relationship("Tag", secondary="note_m2m_tag", backref="notes")
    created = db.Column(db.DateTime, default=datetime.now())


class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(TAG_NAME_LENGTH), nullable=False, unique=True)
    created = db.Column(db.DateTime, default=datetime.now())
