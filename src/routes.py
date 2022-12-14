from flask import render_template, request, flash, redirect
from sqlalchemy.exc import IntegrityError

from . import app
from .repository import contacts


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
            flash('Contact added successfully!')
            return redirect('/contacts')
        except IntegrityError as err:
            print(err)
            return render_template("add_contact.html", message={'error': 'Sorry, but something went wrong: {err}'})
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
            flash('Contact updated successfully!')
            return redirect('/contacts')
        except IntegrityError as err:
            print(err)
            return render_template("edit_contact.html", message={'error': 'Sorry, but something went wrong: {err}'})
    return render_template("edit_contact.html", contact=contacts.get_contact_by_id(cont_id))
