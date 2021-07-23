# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
import sqlalchemy

from . import admin
from .forms import ThoughtForm
from .. import db
from ..models import Thought
from datetime import date
from sqlalchemy import desc


def check_thoughts():
    """
    Prevent non-admins from accessing the page
    """
    if Thought.query.filter_by(date=date.today()).count() >= 10:
        # return render_template('admin/thoughts/thoughts.html',thoughts=thoughts, title="Thoughts")
        return 1


# Thought Views


@admin.route('/thoughts', methods=['GET', 'POST'])
@login_required
def list_thoughts():
    """
    List all thoughts
    """
    # check_admin()
    thoughts = Thought.query.filter_by(thusername=current_user.username).order_by(desc(Thought.date))
    return render_template('admin/thoughts/thoughts.html',
                           thoughts=thoughts, title="Thoughts")


@admin.route('/publicthoughts', methods=['GET', 'POST'])
@login_required
def list_publicthoughts():
    """
    List all thoughts
    """
    # check_admin()
    thoughts = Thought.query.filter_by(is_public= "Yes").order_by(desc(Thought.date))
    # thoughts = thoughts.order_by(date).all()
    # thoughts.sort()
    # thoughts.order_by(date)
    # sorted(thoughts,key= thoughts[1], reverse = True)
    return render_template('admin/thoughts/publicthoughts.html',
                           thoughts=thoughts, title="Public Thoughts")


@admin.route('/thoughts/add', methods=['GET', 'POST'])
@login_required
def add_thought():
    """
    Add a thought to the database
    """
    # check_admin()

    if check_thoughts() == 1:
        flash('Looks like you already added maximum number of thoughts today.🥴 ');
        return redirect(url_for("admin.list_thoughts"))

    add_thought = True

    form = ThoughtForm()
    if form.validate_on_submit():
        thought = Thought(thusername=current_user.username,date=date.today(),
                                th=form.th.data,is_public=form.is_public.data)
        try:
            # add thought to the database
            db.session.add(thought)
            db.session.commit()
            flash('You have successfully added a new thought.')
        except:
            # in case thought date already exists
            flash('Error: There is some error. Try again please.')

        # redirect to thoughts page
        return redirect(url_for('admin.list_thoughts'))

    # load thought template
    return render_template('admin/thoughts/thought.html', action="Add",
                           add_thought=add_thought, form=form,
                           title="Add Thought")


@admin.route('/thoughts/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_thought(id):
    """
    Edit a thought
    """
    # check_admin()

    add_thought = False

    thought = Thought.query.get_or_404(id)
    form = ThoughtForm(obj=thought)
    if form.validate_on_submit():
        thought.thusername=current_user.username
        thought.th = form.th.data
        thought.is_public = form.is_public.data
        db.session.commit()
        flash('You have successfully edited the thought.')

        # redirect to the thoughts page
        return redirect(url_for('admin.list_thoughts'))

    form.th.data = thought.th
    # form.date.data = thought.date
    return render_template('admin/thoughts/thought.html', action="Edit",
                           add_thought=add_thought, form=form,
                           thought=thought, title="Edit Thought")


@admin.route('/thoughts/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_thought(id):
    """
    Delete a thought from the database
    """
    # check_admin()

    thought = Thought.query.get_or_404(id)
    db.session.delete(thought)
    db.session.commit()
    flash('You have successfully deleted the thought.')

    # redirect to the thoughts page
    return redirect(url_for('admin.list_thoughts'))

    return render_template(title="Delete Thought")








#     from flask import *  
# from flask_mail import *  
# from random import *  


# app = Flask(__name__)  
# mail = Mail(app)  
# app.config["MAIL_SERVER"]='smtp.gmail.com'  
# app.config["MAIL_PORT"] = 465      
# app.config["MAIL_USERNAME"] = 'thoughtsandme00@gmail.com'  
# app.config['MAIL_PASSWORD'] = 'luckyOne123@'  
# app.config['MAIL_USE_TLS'] = False  
# app.config['MAIL_USE_SSL'] = True  
# mail = Mail(app)  
# otp = randint(000000,999999)   

# @app.route('/')  
# def index():  
#     return render_template('homepage.html')

# @app.route('/verify',methods = ["POST"])  
# def verify():  
#     email = request.form["email"]   
#     msg = Message('OTP',sender = 'thoughtsandme00@gmail.com', recipients = [email])  
#     msg.body = str(otp)  
#     mail.send(msg)  
#     return render_template('verify.html') 

# @app.route('/validate',methods=["POST"])   
# def validate():  
#     user_otp = request.form['otp']  
#     if otp == int(user_otp):  
#         return "<h3> Email  verification is  successful </h3>"  
#     return "<h3>failure, OTP does not match</h3>"

# if __name__ == '__main__':
#     app.jinja_env.auto_reload = True
#     app.run(debug = True)