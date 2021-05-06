"""CRUD operations."""

from model import db, User, Profile, Comment, connect_to_db


def create_user(username, email, password):
    """Create and return a new user."""

    user = User(username=username, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def get_users():
    """Return all users."""

    return User.query.all()
    

# for showing on url & webpage
def get_user_by_username(username):
    """Return a user by username."""

    # return User.query.get(username)
    return User.query.filter(User.username == username).first()

# for account register/login
def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

# for account register/login
def get_user_by_id(user_id):
    """Return a user by their primary key"""
    
    return User.query.get(user_id)
    # return User.query.filter_by(user_id=user_id).one()
    # return User.query.filter_by(user_id=user_id).first()


def create_profile(about, experience, skill, project, education, contact, user_id):
    """Create and return a new profile."""

    profile = Profile(about=about,
                      experience=experience,
                      skill=skill,
                      project=project,
                      education=education,
                      contact=contact,
                      user_id=user_id)
                

    db.session.add(profile)
    db.session.commit()

    return profile


def get_profile_contents():
    """Return all profiles."""

    return Profile.query.all()

def get_profile_by_id(profile_id):
    """Return a profile by their profile_id."""
    
    return Profile.query.filter_by(profile_id=profile_id).one()
    # return Profile.query.filter_by(profile_id=profile_id).first()


def create_comment(comment, like, profile_id):
    """Create and return a new comment."""

    comment = Comment(comment=comment, like=like, profile_id=profile_id)

    db.session.add(comment)
    db.session.commit()

    return comment


def get_comment_by_id(user_id):
    """Return a comment by their user_id."""
    return Profile.query.filter_by(user_id=user_id).all()


# Functions start here!
if __name__ == '__main__':
    from server import app
    connect_to_db(app)