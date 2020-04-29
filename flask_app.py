#!/home/kmtopel/mysite/env/bin python3
from flask import Flask, render_template, redirect, flash, url_for, request
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import View, Navbar
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from forms import SubmitForm, ContactAdmin
from datetime import datetime as dt
import os

app = Flask(__name__)
csrf = CSRFProtect(app)
bootstrap = Bootstrap(app)
nav = Nav(app)

topbar = Navbar('',
    View('Home', 'main'),
    View('Contact', 'contact'),)

nav.register_element('top',topbar)

key = os.urandom(24)
app.config['SECRET_KEY'] = key

@app.route('/', methods=["GET","POST"])
def main():
    form = SubmitForm(request.form)
    post_title=None
    email=None
    post_type_submit=None
    link=None
    post_time=None
    description=None
    if form.validate_on_submit():
        flash("Success! Thank you for submitting a resource. Your post is being reviewed.")
        post_title = form.post_title.data
        email = form.email.data
        post_time = dt.today().strftime('%m/%d/%Y')
        description = form.description.data
        post_type_submit = form.post_type_submit.data
        link = form.link.data
        return redirect(url_for('main'))
    form.post_title.data = ''
    form.email.data = ''
    form.description.data=''
    form.post_type_submit.data=''
    form.link.data=''
    return render_template('main.html',form=form, post_title=post_title, post_time=post_time, description=description, link=link, post_type=post_type_submit, email=email)

@app.route('/contact', methods=["GET","POST"])
def contact():
    form = ContactAdmin()
    return render_template('contact.html',form=form)

nav.init_app(app)