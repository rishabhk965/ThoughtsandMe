# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from datetime import date
from wtforms.widgets import TextArea

class ThoughtForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    date = date.today()
    th = StringField('Thought', validators=[DataRequired()], widget=TextArea())
    is_public = SelectField('Personal / Public', choices = [("No",'Personal Thought'),("Yes",'Post your Thought')], validators=[DataRequired()])
    submit = SubmitField('Submit')