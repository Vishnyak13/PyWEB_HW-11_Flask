from src import models, db
import datetime


def create_contacts(first_name, last_name, email, phone, birthday, address):
    birth_format = datetime.datetime.strptime(birthday, '%Y-%m-%d')
    contact = models.Contact(first_name=first_name, last_name=last_name, email=email, phone=phone,
                             birthday=birth_format.date(), address=address, created=datetime.datetime.now().date())
    db.session.add(contact)
    db.session.commit()


def update_contacts(cont_id, first_name, last_name, email, phone, birthday, address):
    birth_format = datetime.datetime.strptime(birthday, '%Y-%m-%d')
    contact = models.Contact.query.filter_by(id=cont_id).first()
    contact.first_name = first_name
    contact.last_name = last_name
    contact.email = email
    contact.phone = phone
    contact.birthday = birth_format.date()
    contact.address = address
    db.session.commit()


def delete_contacts(first_name, last_name):
    contact = models.Contact.query.filter_by(first_name=first_name, last_name=last_name).first()
    db.session.delete(contact)
    db.session.commit()


def get_contact_by_id(cont_id):
    contact = models.Contact.query.filter_by(id=cont_id).first()
    return contact


def get_all_contacts():
    contacts = models.Contact.query.all()
    return contacts