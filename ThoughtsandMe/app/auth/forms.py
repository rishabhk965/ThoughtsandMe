# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from flask_login import current_user
from wtforms.validators import DataRequired, Email, EqualTo , Length

from ..models import User

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password') , Length(min=6)])

    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')


class EditRegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email (Cannot be modified)', validators=[DataRequired()], render_kw={'readonly': True})
    username = StringField('Username (Cannot be modified)', validators=[DataRequired()], render_kw={'readonly': True})
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    change = SubmitField('Change Password')
    submit = SubmitField('Save')

class verifyy(FlaskForm):
    submit = SubmitField('Send OTP on my registered email.')

class verifyynew(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send OTP on my email.')

class Verf(FlaskForm):
    otp = StringField('OTP' , validators=[DataRequired()])
    submit = SubmitField('Verify')

class newp(FlaskForm):
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Change Password')

class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    change = SubmitField('Forgot Password')
    submit = SubmitField('Login to your account')