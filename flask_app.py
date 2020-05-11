#!/home/kmtopel/mysite/env/bin python3
from flask import Flask, render_template, redirect, flash, url_for, request
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from forms import SubmitForm, ContactAdmin
from datetime import datetime as dt
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

csrf = CSRFProtect(app)
bootstrap = Bootstrap(app)
nav = Nav(app)
db = SQLAlchemy(app)

class Posts(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime,nullable=True)
    post_title = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(120),nullable=False)
    link = db.Column(db.String(120))
    post_type = db.Column(db.String(80),nullable=False)
    description = db.Column(db.Text)
    active = db.Column(db.Boolean, default=0)
    sql_autoincrement=True

key = os.urandom(24)
app.config['SECRET_KEY'] = key

choices = ['Show All','Information','Financial','Food','Health Care','Employment/Vocational','Social Service','Education','Other']

@app.route('/', methods=["GET","POST"])
def main():
    form = SubmitForm(request.form)
    if form.validate_on_submit():
        flash("Success! Thank you for submitting a resource. Your post is being reviewed.")
        post = Posts(
            post_title=form.post_title.data,
            email=form.email.data,
            description=form.description.data,
            post_type=form.post_type_submit.data,
            link = form.link.data,
            timestamp=dt.utcnow()
                )
        db.session.add_all([post])
        db.session.commit()
        return redirect(url_for('main'))
    data=Posts.query.all()
    return render_template('main.html',form=form, data=data, choices=choices)

@app.route('/contact', methods=["GET","POST"])
def contact():
    form = ContactAdmin()
    return render_template('contact.html',form=form)