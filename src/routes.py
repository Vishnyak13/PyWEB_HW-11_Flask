from flask import render_template, request, flash, redirect
from sqlalchemy.exc import IntegrityError

from . import app
from .repository import contacts, notes


@app.route("/healthcheck", strict_slashes=False)
def healthcheck():
    return 'I am alive and running!'


@app.route("/", strict_slashes=False)
def index():
    return render_template("index.html")


@app.route("/contacts", strict_slashes=False)
def contact_page():
    contacts_all = contacts.get_all_contacts()
    return render_template("contacts.html", contacts=contacts_all)


@app.route("/add_contact", strict_slashes=False, methods=['POST', 'GET'])
def add_contact():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        birthday = request.form['birthday']
        address = request.form['address']
        try:
            contacts.create_contacts(first_name, last_name, email, phone, birthday, address)
            flash(f'Contact {first_name} {last_name} added successfully!')
            return redirect('/contacts')
        except IntegrityError as err:
            print(err)
            return render_template("add_contact.html", message={'error': f'Sorry, but something went wrong: {err}'})
    return render_template("add_contact.html")


@app.route("/edit_contact/<cont_id>", strict_slashes=False, methods=['POST', 'GET'])
def edit_contact(cont_id):
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        birthday = request.form['birthday']
        address = request.form['address']
        try:
            contacts.update_contacts(cont_id, first_name, last_name, email, phone, birthday, address)
            flash(f'Contact {first_name} {last_name} updated successfully!')
            return redirect('/contacts')
        except IntegrityError as err:
            print(err)
            return render_template("edit_contact.html", message={'error': f'Sorry, but something went wrong: {err}'})
    return render_template("edit_contact.html", contact=contacts.get_contact_by_id(cont_id))


@app.route("/delete_contact/<cont_id>", strict_slashes=False)
def delete_contact(cont_id):
    contacts.delete_contacts(cont_id)
    flash('Contact deleted successfully!')
    return redirect('/contacts')


@app.route("/notes", strict_slashes=False)
def notes_page():
    notes_all = notes.get_all_notes()
    return render_template("notes.html", notes=notes_all)


@app.route("/add_note", strict_slashes=False, methods=['POST', 'GET'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        tags = request.form.getlist('tags')
        try:
            notes.create_notes(title, text, tags)
            flash(f'Note {title} added successfully!')
            return redirect('/notes')
        except IntegrityError as err:
            print(err)
            return render_template("add_note.html", message={'error': f'Sorry, but something went wrong: {err}'})
    return render_template("add_note.html", tags=notes.get_all_tags())


@app.route("/add_tag", strict_slashes=False, methods=['POST', 'GET'])
def add_tag():
    if request.method == 'POST':
        name = request.form['name']
        notes.add_tag(name)
        flash(f'Tag {name} added successfully!')
        return redirect('/notes')
    return render_template("add_tag.html")


@app.route("/edit_note/<note_id>", strict_slashes=False, methods=['POST', 'GET'])
def edit_note(note_id):
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        tags = request.form.getlist('tags')
        try:
            notes.update_notes(note_id, title, text, tags)
            flash(f'Note {title} updated successfully!')
            return redirect('/notes')
        except IntegrityError as err:
            print(err)
            return render_template("edit_note.html", message={'error': f'Sorry, but something went wrong: {err}'})
    return render_template("edit_note.html", note=notes.get_note_by_id(note_id), tags=notes.get_all_tags())


@app.route("/delete_note/<note_id>", strict_slashes=False)
def delete_note(note_id):
    notes.delete_notes(note_id)
    flash('Note deleted successfully!')
    return redirect('/notes')
