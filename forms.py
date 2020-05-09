from wtforms.fields import TextAreaField, SelectField, SubmitField, StringField
from wtforms.validators import InputRequired, Email
from flask_wtf import FlaskForm

choice_list = [(None, '--Please select an option--'),('Information','Information'),('Financial','Financial'),('Food','Food'),('Health Care','Health Care'),('Employment/Vocational','Employment/Vocational'),('Social Service','Social Service'),('Education','Education'),('Other','Other')]
choice_sans_blank = [('Show All', 'Show All'),('Information','Information'),('Financial','Financial'),('Food','Food'),('Health Care','Health Care'),('Employment/Vocational','Employment/Vocational'),('Social Service','Social Service'),('Education','Education'),('Other','Other')]

class SubmitForm(FlaskForm):
    email = StringField('Email',validators=[Email(),InputRequired()])
    post_title = StringField('Post Title', validators=[InputRequired()])
    post_type_submit = SelectField('Type',choices=choice_list, validators=[InputRequired()])
    link = StringField('Link')
    description = TextAreaField('Description',validators=[InputRequired()])
    submit_btn = SubmitField('Submit')

class FilterResults(FlaskForm):
    post_type_filter = SelectField('Filter Results:',choices=choice_sans_blank)
    apply_filter = SubmitField('Apply')

class ContactAdmin(FlaskForm):
    email = StringField('Email',validators=[Email()])
    msg = TextAreaField('Message',validators=[InputRequired()])
    submit_btn = SubmitField('Send Message')
