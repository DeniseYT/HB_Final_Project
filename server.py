"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
from crud import get_user_by_email, get_user_by_username, create_profile, get_profile_by_about
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
        # user = crud.get_user_by_email(email)
        user = crud.get_user_by_username(username) # both works
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
        session['user'] = user.username # works
        session['user_id'] = user.user_id #show user_id
        flash('Logged in.')
        return redirect('/build')

    else:
        flash('incorrect login')
        return redirect('/account')


# just testing and working fine
# @app.route('/user')
# def user():
#     """username shows in url."""

#     if "user" in session:
#         user = session["user"]

#     return f"<h1>{user}</h1>"


@app.route('/build')
def build_new():
    """Build a new content."""

    profiles = crud.get_profiles()
    return render_template('build_your_own.html', profiles=profiles)
    
    # session['user'] = user.user_id
    # username = session['user']
    # profile = crud.get_profile_by_user_id(user_id)
    # return render_template('build_your_own.html', profile=profile) 
    # second user_id = variable name


@app.route('/build', methods=['POST'])
def build_new_content():

    about = request.form.get("about") #dictionary key "about"
    experience = request.form.get("experience")
    project = request.form.get("project")
    skill = request.form.get("skill")
    education = request.form.get("education")
    contact = request.form.get("contact")
    user_id = session.get("user_id")

    # profile = crud.create_profile(about=about, experience=experience, skill=skill, project=project, education=education, contact=contact, user_id=user_id)
    # profiles = crud.get_profiles()

    print(session)

    profile_content = crud.create_profile(about=about,
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


@app.route('/add_comment', methods=['POST'])
def add_comment():

    user_id = session.get("user_id")
    # profile_id = request.form.get("profile_id")
    comment = request.form.get("comment")

    user_id = crud.get_user_by_id(user_id)
    profile_id = crud.get_profile_by_id(profile_id)
    add_comment = crud.create_comment(comment=comment, like=like, prodile_id=profile_id)

    flash("Your Comment has been added")
    return redirect('/')



@app.route('/profile/view/<username>')
def personal_profile(username):

    # test ok in -i 
    # username = get_user_by_username("test1") ---> "test1"
    # user_id = get_user_by_username("test1").user_id ---> "1"
    # username = get_profile_by_user_id("1").username ---> "1"
    # username = get_profile_by_profile_id("1").username ---> "1"

    username = crud.get_user_by_username(username)
    user_id = get_user_by_username(username).user_id
    # user_id = crud.get_user_by_username(username) # same as above

    return render_template('homepage.html', user_id=user_id)


@app.route('/profile/view/<username>')
def view_personal_profile(username):

    # test ok in -i 
    # user = get_user_by_id("1") ---> user.user_id ---> 1
    # user = get_profile_by_user_id("1") ---> user[0] ---> user's profile

    # user_id = crud.get_user_by_id(user_id)
    # profile_id = crud.get_profile_by_profile_id(profile_id)
    # profile_id = crud.get_profiles()

    # profile_content = crud.create_profile(about=about,
    #                               experience=experience,
    #                               skill=skill,
    #                               project=project,
    #                               education=education,
    #                               contact=contact,
    #                               user_id=user_id)

    # print(profile_about)

    # if profile_about:
    #     return f"{profile_about} profile found"
    # else: 
    #     return f"No profile found"
    
    # print(profile_id)
    
    # if profile_id:
    #     return f"{profile_id} profile found"
    # else: 
    #     return f"No profile found"
    


# @app.route('/add_comment', methods=['POST'])
# def add_comment():
    """User adding a comment to a profile"""

    # user_id = session.get("user_id")
    # # profile_id = request.form.get("profile_id")
    # comment = request.form.get("comment")

    # user_id = crud.get_user_by_id(user_id)
    # profile_id = crud.get_profile_by_id(profile_id)
    # add_comment = crud.create_comment(comment=comment, like=like, prodile_id=profile_id)

    # flash("Your Comment has been added")
    # return redirect('/')


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