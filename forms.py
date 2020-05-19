from wtforms.fields import TextAreaField, SelectField, SubmitField, StringField
from wtforms.validators import InputRequired, Email
from flask_wtf import FlaskForm

choice_list = [(None, '--Please select an option--'),('Information','Information'),('Financial','Financial'),('Food','Food'),('Health Care','Health Care'),('Employment/Vocational','Employment/Vocational'),('Fitness/Recreation','Fitness/Recreation'),('Mental Health/Substance Abuse','Mental Health/Substance Abuse'),('Social Service','Social Service'),('Education','Education'),('Transportation','Transportation'),('Personal Care','Personal Care'),('Child Care','Child Care'),('Disability Services','Disability Services'),('Other','Other')]

class SubmitForm(FlaskForm):
    email = StringField('Email',validators=[Email(),InputRequired()])
    post_title = StringField('Post Title', validators=[InputRequired()])
    post_type_submit = SelectField('Type',choices=choice_list, validators=[InputRequired()])
    link = StringField('Link')
    ph_num = StringField('Resource Phone Number')
    description = TextAreaField('Description',validators=[InputRequired()])
    submit_btn = SubmitField('Submit')

class ContactAdmin(FlaskForm):
    email = StringField('Email',validators=[Email()])
    msg = TextAreaField('Message',validators=[InputRequired()])
    submit_btn = SubmitField('Send Message')
