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


def get_profiles():
    """Return all profiles."""

    return Profile.query.all()


def create_comment(profile_id, comment, like):
    """Create and return a new comment."""

    comment = Comment(profile_id=profile_id, comment=comment, like=like)

    db.session.add(comment)
    db.session.commit()

    return comment


# Functions start here!
if __name__ == '__main__':
    from server import app
    connect_to_db(app)