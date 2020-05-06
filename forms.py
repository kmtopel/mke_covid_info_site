from wtforms.fields import TextAreaField, SelectField, SubmitField, StringField
from wtforms.validators import InputRequired, Email, Required
from flask_wtf import FlaskForm

choice_list = [(None, '--Please select an option--'),('Information','Information'),('Financial Assistance','Financial Assistance'),('Health Care','Health Care'),('Food','Food'),('Employment/Vocational','Employment/Vocational'),('Mental Health/Social Service','Mental Health/Social Service'),('Housing','Housing'),('Education','Education'),('Other','Other')]
choice_sans_blank = [('Show All', 'Show All'),('Information','Information'),('Financial Assistance','Financial Assistance'),('Health Care','Health Care'),('Food','Food'),('Employment/Vocational','Employment/Vocational'),('Mental Health/Social Service','Mental Health/Social Service'),('Housing','Housing'),('Education','Education'),('Other','Other')]

class SubmitForm(FlaskForm):
    email = StringField('Email',validators=[Email(),InputRequired()])
    post_title = StringField('Post Title', validators=[InputRequired()])
    post_type_submit = SelectField('Type',choices=choice_list, validators=[Required()])
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
