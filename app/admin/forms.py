# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired
from datetime import date
from wtforms.widgets import TextArea

class ThoughtForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    date = date.today()
    th = StringField('Thought', validators=[DataRequired()], widget=TextArea() , render_kw={'style': 'height: 30ch'})
    is_public = RadioField('Personal / Public', choices = [("No",'Personal Thought (Only visible to you)'),("Yes",'Post your Thought (Visible to everyone)')], validators=[DataRequired()] , default="No" )
    submit = SubmitField('Submit')