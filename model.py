"""Models for personal webite app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    # comments = a list of comment objects

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Profile(db.Model):
    """A profile."""

    __tablename__ = 'profiles'

    profile_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    about = db.Column(db.Text)
    experience = db.Column(db.Text)
    skill = db.Column(db.Text)
    project = db.Column(db.Text)
    education = db.Column(db.Text)
    contact = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id')) 
    # because one user has one profile, so we connect two tables

    # comments = a list of comment objects

    def __repr__(self):
        return f'<Profile profile_id={self.profile_id} about={self.about}>'


class Comment(db.Model):
    """A comment."""

    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    comment = db.Column(db.String)
    like = db.Column(db.Integer)
    # user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.profile_id'))

    user = db.relationship('User', backref='comments')
    profile = db.relationship('Profile', backref='comments')

    def __repr__(self):
        return f'<Comment comment_id={self.comment_id} comment={self.comment}>'


def connect_to_db(flask_app, db_uri='postgresql:///profiles', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)