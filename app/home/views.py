# app/home/views.py

from flask import render_template
from flask_login import login_required

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html')


@home.route('/about')
def about():
    """
    Render the homepage template on the / route
    """
    return render_template('home/about.html', title="About")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

# from flask import *  
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
# def indexx():  
#     return render_template('homepage.html' , title="Verify")

# class verf():  

#     @app.route('/verify',methods = ["POST"])  
#     def verify(emailll):  
#         email = emailll   
#         msg = Message('OTP',sender = 'username@gmail.com', recipients = [email])  
#         msg.body = str(otp)  
#         mail.send(msg)  
#         return render_template('verify.html' , title = "Verify")  


#     # @app.route('/validate',methods=["POST"])   
#     def validate():  
#         user_otp = request.form['otp']  
#         if otp == int(user_otp):  
#             return "<h3> Email  verification is  successful </h3>"  
#         return "<h3>failure, OTP does not match</h3>"   


# if __name__ == '__main__':  
#     app.run(debug = True) 
