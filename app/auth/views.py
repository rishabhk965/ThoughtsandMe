# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user , current_user

from . import auth 
from .forms import LoginForm, RegistrationForm, EditRegistrationForm , Verf , verifyy , newp , verifyynew
from .. import db
from ..models import User
import smtplib
from random import *

# idd= 0
ootp = randint(100010,992999) 
cotp=str(ootp)
# useremail = "wevh"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = User(email=form.email.data,
                            username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            password=form.password.data,
                            country=form.country.data)

        # useremail = employee.email
        # add employee to the database
        db.session.add(employee)
        db.session.commit()
        # verify(form.email.data)
        flash('You have successfully registered! Please check your email for OTP.')

        # verf.indexx()
        # verf.verify(form.email.data)
        # verf.validate()
        s = smtplib.SMTP('smtp.gmail.com', 587)
  
        # start TLS for security
        s.starttls()
        
        # Authentication
        s.login("thoughtsandme00@gmail.com", "luckyOne123@")
        
        # message to be sent  
        
        # sending the mail
        s.sendmail("thoughtsandme00@gmail.com", employee.email,'Subject: {}\n\n{}'.format("Email Verification","Good to know that you registered at Thoughts and Me. Your OTP is " + cotp + ". \n Enjoy our website. "))
        
        # terminating the session
        s.quit()
        login_user(employee)

        # redirect to the login page
        return redirect(url_for('auth.verf'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')

@auth.route('/verify', methods=['GET', 'POST'])
def verify():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """

    # idd=current_user.id
    employee = User.query.filter_by(email = current_user.email).first_or_404()
    form = verifyy(obj = employee)
    if form.validate_on_submit():
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()
        
        # Authentication
        s.login("thoughtsandme00@gmail.com", "luckyOne123@")
        
        # message to be sent 
        ootp = randint(100010,992999) 
        cotp=str(ootp) 
        
        # sending the mail
        s.sendmail("thoughtsandme00@gmail.com", current_user.email,'Subject: {}\n\n{}'.format("Email Verification","Good to know that you registered at Thoughts and Me. Your OTP is "  + cotp + ". \n Enjoy our website. "))
        useremail = current_user.email
        
        # terminating the session
        s.quit()

            # redirect to the login page
        flash('Otp sent on your registered email id.')
        return redirect(url_for('auth.verf'))

    # load registration template
    return render_template('auth/verify.html', form=form, title='Verify')


@auth.route('/forgot3', methods=['GET', 'POST'])
def forgot3():
    employee = User.query.get_or_404(current_user.id)
    form = newp(obj = employee)
    if form.validate_on_submit():
        employee.password=form.password.data

        # add employee to the database
        db.session.commit()
            # redirect to the login page
        flash('Successfully changed your password.')
        return redirect(url_for('home.dashboard'))
        
    return render_template('auth/forgot3.html', form=form, title='Login')

@auth.route('/forgotnew3/<y>', methods=['GET', 'POST'])
def forgotnew3(y):
    x = User.query.filter_by(email = y).first()
    employee = User.query.get_or_404(x.id)
    form = newp(obj = employee)
    if form.validate_on_submit():
        employee.password=form.password.data

        # add employee to the database
        db.session.commit()
            # redirect to the login page
        flash('Successfully changed your password.')
        return redirect(url_for('auth.login'))
        
    return render_template('auth/forgotnew3.html', form=form, title='Login')


@auth.route('/forgot2/<x>', methods=['GET', 'POST'])
def forgot2(x):
    form = Verf()
    if form.validate_on_submit():
        if form.otp.data == x :
            return redirect(url_for('auth.forgot3'))
        else:
            flash('Wrong OTP, Try again later.')
            return redirect(url_for('home.dashboard'))

    return render_template('auth/forgot2.html', form=form, title='Login')


@auth.route('/forgotnew2/<x>/<y>', methods=['GET', 'POST'])
def forgotnew2(x, y):
    form = Verf()
    if form.validate_on_submit():
        if form.otp.data == x :
            return redirect(url_for('auth.forgotnew3' , y = y))
        else:
            flash('Wrong OTP, Try again later.')
            return redirect(url_for('home.dashboard'))

    return render_template('auth/forgotnew2.html', form=form, title='Login')


@auth.route('/forgot', methods=['GET', 'POST'])
def forgot():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    employee = User.query.filter_by(email = current_user.email).first_or_404()
    form = verifyy(obj = employee)
    if form.validate_on_submit():
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()
        
        # Authentication
        s.login("thoughtsandme00@gmail.com", "luckyOne123@")
        
        # message to be sent 
        ootp2 = randint(100010,992999) 
        ctp=str(ootp2) 
        
        # sending the mail
        s.sendmail("thoughtsandme00@gmail.com", current_user.email,'Subject: {}\n\n{}'.format("Password Change","Good to know that you registered at Thoughts and Me. Your OTP is "  + ctp + ". \n Enjoy our website."))
        
        # terminating the session
        s.quit()

        return redirect(url_for('auth.forgot2' , x = ctp))

    # load registration template
    return render_template('auth/forgot.html', form=form, title='Change Password')


@auth.route('/forgotnew', methods=['GET', 'POST'])
def forgotnew():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    form = verifyynew()
    if form.validate_on_submit():
        employee = User.query.filter_by(email = form.email.data).first_or_404()
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()
        
        # Authentication
        s.login("thoughtsandme00@gmail.com", "luckyOne123@")
        
        # message to be sent 
        ootp2 = randint(100010,992999) 
        ctp=str(ootp2) 
        
        # sending the mail
        s.sendmail("thoughtsandme00@gmail.com", form.email.data, 'Subject: {}\n\n{}'.format("Password Change","Good to know that you registered at Thoughts and Me. Your OTP is "  + ctp + ". \n Enjoy our website. "))
        
        # terminating the session
        s.quit()

        return redirect(url_for('auth.forgotnew2' , x = ctp , y = form.email.data))

    # load registration template
    return render_template('auth/forgotnew.html', form=form, title='Change Password')



@auth.route('/verf', methods=['GET', 'POST'])
def verf():
    employee = User.query.get_or_404(current_user.id)
    form = Verf(obj=employee)
    if form.validate_on_submit():
        if form.otp.data == cotp :
            employee.verify = 1
            db.session.commit()
            flash('Congrats , you are a verified user now.')
            return redirect(url_for('home.dashboard'))

            # when login details are incorrect
        else:
            flash('OTP is wrong, Kindly try again')
            if current_user.is_authenticated :
                return redirect(url_for('home.dashboard'))
            else :
                return redirect(url_for('auth.login'))

    # load login template
    return render_template('auth/verf.html', form=form, title='Verification')

@auth.route('/edit<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    employee = User.query.get_or_404(id)
    form = EditRegistrationForm(obj=employee)
    if form.validate_on_submit():
        if form.change.data:
            return redirect(url_for('auth.forgot'))
        employee.first_name=form.first_name.data
        employee.last_name=form.last_name.data
        employee.country=form.country.data

        # add employee to the database
        db.session.commit()
        flash('You have successfully edited your profile!')

        # redirect to the login page
        return redirect(url_for('home.dashboard'))
    

    # load registration template
    return render_template('auth/edit.html', form=form, title='EditUser')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():
        if form.change.data:
            return redirect(url_for('auth.forgotnew'))

        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        employee = User.query.filter_by(email=form.username.data).first()
        if employee is not None and employee.verify_password(
                form.password.data):
            # log employee in
            login_user(employee)

            # redirect to the dashboard page after login
            return redirect(url_for('home.dashboard'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))