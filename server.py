"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
from crud import get_user_by_email
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""

    # just testing ok
    # users = crud.get_users()
    # oneUser = crud.get_user_by_username("test1") 
    # return render_template('homepage.html', users=users, oneUser=oneUser)

    return render_template('homepage.html')


@app.route('/<usr>')
def user(usr):
    """username shows in url."""

    return f"<h1>{usr}</h1>"


@app.route('/build')
def build_new():
    """Build a new content."""

    contents = crud.get_profile_contents()
    return render_template('build_your_own.html', contents=contents)
   
    # username = session['user']
    # profile = crud.get_profile_by_user_id(user_id)
    # return render_template('build_your_own.html', profile=profile) 
    #second user_id = variable name


@app.route('/build', methods=['POST'])
def build_new_content():

    about = request.form.get("about")
    experience = request.form.get("experience")
    project = request.form.get("project")
    skill = request.form.get("skill")
    education = request.form.get("education")
    contact = request.form.get("contact")
    user_id = session.get("user_id")

    # profile = crud.create_profile(about=about, experience=experience, skill=skill, project=project, education=education, contact=contact, user_id=user_id)
    # contents = crud.get_profile_contents()

    profile = crud.create_profile(about=about,
                                  experience=experience,
                                  skill=skill,
                                  project=project,
                                  education=education,
                                  contact=contact,
                                  user_id=user_id)

    profile_about = crud.get_profile_by_about(about)
    session["about"] = profile_about.about

    profile_experience = crud.get_profile_by_experience(experience)
    session["experience"] = profile_experience.experience

    profile_project = crud.get_profile_by_project(project)
    session["project"] = profile_project.project

    profile_skill = crud.get_profile_by_skill(skill)
    session["skill"] = profile_skill.skill

    profile_education = crud.get_profile_by_education(education)
    session["education"] = profile_education.education

    profile_contact = crud.get_profile_by_contact(contact)
    session["contact"] = profile_contact.contact


    # input_username = request.form.get('username')
    # user = crud.get_user_by_username(input_username)
    # session["user"] = user.username


    flash("Your profile has been added")

    return redirect ('/')
    # return redirect ('/build')
    # return render_template('homepage.html', profile=profile, contents=contents)
                                 
    # else:
    #     return render_template('build_your_own.html')



@app.route('/account')
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template('account.html', users=users)


@app.route('/account', methods=['POST'])
def register_users():
    """Create a new user."""

    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user:
        flash('Email has already taken. Try again')
        return redirect('/account')

    else:
        crud.create_user(username, email, password)
        user = crud.get_user_by_email(email)
        session['user'] = user.username
        flash('Your account has been created.')
        return redirect('/build')


@app.route('/login', methods=['POST'])
def user_login():
    """Login user"""

    input_email = request.form.get('email')
    input_password = request.form.get('password')

    user = crud.get_user_by_email(input_email)

    if user and user.password == input_password:
        session['user'] = user.username
        flash('Logged in.')
        return redirect('/build')

    else:
        flash('incorrect login')
        return redirect('/account')


# @app.route("/", methods=['POST'])
# def add_comment():
#     """User adding a comment to a profile"""

#     user_id = session.get("user_id")
#     profile_id = request.form.get("profile_id")
#     comment = request.form.get("comment")


#     profile = crud.get_blog_by_id(profile_id)

#     add_comment = crud.create_comment(comment=comment, like=like, prodile_id=profile_id)

#     flash("Your Comment has been added")

#     return redirect('/')


# @app.route("/", methods=['POST'])
# def add_comment():
#     """User adding a like to a profile"""

#     user_id = session.get("user_id")
#     profile_id = request.form.get("profile_id")
#     like = request.form.get("like")

#     profile = crud.get_blog_by_id(profile_id)

#     add_like = crud.create_comment(comment=comment, like=like, prodile_id=profile_id)

#     flash("You like it")

#     return redirect('/')

 




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)