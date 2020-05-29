#!/home/kmtopel/mysite/env/bin python3
from flask import Flask, render_template, redirect, flash, url_for, request, Markup, jsonify
from flask_nav import Nav
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from forms import SubmitForm, ContactAdmin
from datetime import datetime as dt
import smtplib
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

csrf = CSRFProtect(app)
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
    ph_num = db.Column(db.String(80),nullable=True)
    sql_autoincrement=True

class Messages(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    email = db.Column(db.String(80))
    msg = db.Column(db.Text)

key = os.urandom(24)
app.config['SECRET_KEY'] = key

choices = ['Show All','Information','Financial','Food','Health Care','Employment/Vocational','Utilities','Housing/Rent Assistance','Fitness/Recreation','Mental Health/Substance Abuse','Social Service','Education','Transportation','Personal Care','Child Care','Disability Services','Other']

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
            ph_num = form.ph_num.data,
            timestamp=dt.utcnow()
                )
        db.session.add_all([post])
        db.session.commit()
        return redirect(url_for('main'))
    data=Posts.query.order_by(Posts.timestamp.desc()).all()
    return render_template('main.html',form=form, data=data, choices=choices)

@app.route('/contact', methods=["GET","POST"])
def contact():
    form = SubmitForm(request.form)
    contact = ContactAdmin(request.form)
    if contact.validate_on_submit():
        flash(Markup("<strong>Thank you!</strong> Your message has been sent."))
        msg = Messages(
                timestamp=dt.utcnow(),
                email = contact.email.data,
                msg = contact.msg.data
                )
        db.session.add_all([msg])
        db.session.commit()
        return redirect(url_for('contact'))

    if form.validate_on_submit():
        flash(Markup("<strong>Success!</strong> Thank you for submitting a resource. Your post is being reviewed."))
        post = Posts(
            post_title=form.post_title.data,
            email=form.email.data,
            description=form.description.data,
            post_type=form.post_type_submit.data,
            link = form.link.data,
            ph_num = form.ph_num.data,
            timestamp=dt.utcnow()
                )
        db.session.add_all([post])
        db.session.commit()
        return redirect(url_for('contact'))
    return render_template('contact.html', contact=contact, form=form)

# @app.route('/api',methods=['GET'])
# def api():
#     return jsonify(Posts.query.order_by(Posts.timestamp.desc()).all().to_dict())