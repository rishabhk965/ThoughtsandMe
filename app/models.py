# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(UserMixin, db.Model):
    """
    Create an User table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    country = db.Column(db.String(60))
    verify = db.Column(db.Integer , default=0)
    thoughts_id = db.Column(db.Integer, db.ForeignKey('thoughts.id'))
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)
        

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Thought(db.Model):
    """
    Create a Thought table
    """

    __tablename__ = 'thoughts'

    id = db.Column(db.Integer, primary_key=True)
    th = db.Column(db.Text(10000))
    thusername = db.Column(db.String(60), index=True)
    date = db.Column(db.String(11))
    # time = db.Column(db.String(11))
    is_public = db.Column(db.String(4))
    # description = db.Column(db.String(200))
    users = db.relationship('User', backref='thought',
                                lazy='dynamic')
    def __repr__(self):
        return '<Thought: {}>'.format(self.th)


# class Like(db.Model):
#     """
#     Create a Like table
#     """

#     __tablename__ = 'likes'

#     id = db.Column(db.Integer, primary_key=True)
#     thid = db.Column(db.Integer)
#     thlike = db.Column(db.Integer, primary_key=True)
#     employees = db.relationship('Employee', backref='role',
#                                 lazy='dynamic')

#     def __repr__(self):
#         return '<Role: {}>'.format(self.name)

 
