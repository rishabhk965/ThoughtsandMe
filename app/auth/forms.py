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
    email = StringField('Email', validators=[DataRequired(), Email()] , render_kw={'style': 'width: 60ch'})
    username = StringField('Username', validators=[DataRequired()] , render_kw={'style': 'width: 60ch'})
    first_name = StringField('First Name', validators=[DataRequired()] , render_kw={'style': 'width: 60ch'})
    last_name = StringField('Last Name', validators=[DataRequired()] , render_kw={'style': 'width: 60ch'})
    country = StringField('Country', validators=[DataRequired()] , render_kw={'style': 'width: 60ch'})
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password') , Length(min=6)] , render_kw={'style': 'width: 60ch'})

    confirm_password = PasswordField('Confirm Password', render_kw={'style': 'width: 60ch'})
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
    email = StringField('Email (Cannot be modified)', validators=[DataRequired()], render_kw={'readonly': True, 'style' : 'width: 60ch'})
    username = StringField('Username (Cannot be modified)', validators=[DataRequired()], render_kw={'readonly': True, 'style' : 'width: 60ch'})
    first_name = StringField('First Name', validators=[DataRequired()] , render_kw={'style': 'width: 60ch'})
    last_name = StringField('Last Name', validators=[DataRequired()] , render_kw={'style': 'width: 60ch'})
    country = StringField('Country', validators=[DataRequired()] , render_kw={'style': 'width: 60ch'})
    change = SubmitField('Change Password')
    submit = SubmitField('Save')

class verifyy(FlaskForm):
    email = StringField('Email', validators=[DataRequired()], render_kw={'readonly': True , 'style' : 'width: 60ch'})
    submit = SubmitField('Send OTP on my registered email.')

class verifyynew(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()] , render_kw={'style': 'width: 60ch'})
    submit = SubmitField('Send OTP on my email.')

class Verf(FlaskForm):
    otp = StringField('OTP' , validators=[DataRequired()] , render_kw={'style': 'width: 60ch'})
    submit = SubmitField('Verify')

class newp(FlaskForm):
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ] , render_kw={'style': 'width: 60ch'})
    confirm_password = PasswordField('Confirm Password' , render_kw={'style': 'width: 60ch'})
    submit = SubmitField('Change Password')

class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()] , render_kw={'style': 'width: 60ch'})
    password = PasswordField('Password', validators=[DataRequired()] , render_kw={'style': 'width: 60ch'})
    change = SubmitField('Forgot Password')
    submit = SubmitField('Login to your account')