"""CRUD operations."""

from model import db, User, Profile, Comment, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def get_users():
    """Return all users."""

    return User.query.all()
    

# for showing on url & webpage
def get_user_by_username(username):
    """Return a user by username."""

    return User.query.get(username)

# for account register/login
def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

# for account register/login
def get_user_by_id(user_id):
    """Return a user by their primary key"""
    return User.query.get(user_id)


def create_profile(about, experience, skill, project, education, contact):
    """Create and return a new profile."""

    profile = Profile(about=about,
                      experience=experience,
                      skill=skill,
                      project=project,
                      education=education,
                      contact=contact)

    db.session.add(profile)
    db.session.commit()

    return profile


def get_profiles():
    """Return all profiles."""

    return Profile.query.all()


def create_comment(user, profile, comment, like):
    """Create and return a new comment."""

    comment = Comment(user=user, profile=profile, comment=comment, like=like)

    db.session.add(comment)
    db.session.commit()

    return comment


# Functions start here!
if __name__ == '__main__':
    from server import app
    connect_to_db(app)