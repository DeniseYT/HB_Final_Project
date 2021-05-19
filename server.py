from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
from crud import get_user_by_email, get_user_by_username
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


@app.route('/<username>')
def user_homepage(username):
    """View particular user's homepage"""

    # session['user'] = user.username
    user = crud.get_user_by_username(username)
    return render_template('homepage.html',user=user)


# @app.route('/profile')
# def profile():
#     """View profile built page."""

#     return render_template('homepage.html')


# React
@app.route("/profile/Denise")
def show_user_profile():
    """Show particular user's profile"""

    return render_template("user_profile_data.html")


@app.route('/account')
def all_users():
    """View all users."""

    return render_template('account.html')


@app.route('/account', methods=['POST'])
def register_users():
    """Create a new user."""

    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    if email in crud.get_all_emails():
        flash('Email has already taken. Try again')
        return redirect('/account')

    else:
        crud.create_user(username, email, password)
        user = crud.get_user_by_username(username) 
        session['user'] = user.username
        flash('Your account has been created.')
        return redirect(f'/build/{user.username}')


@app.route('/login')
def show_login():

    if session['user']:
        flash('You are already logged in')
        return redirect('/build')

    return render_template('account.html')


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
        return redirect(f'/build/{user.username}')

    else:
        flash('incorrect login')
        return redirect('/account')


@app.route('/logout')
def user_logout():
    # remove the username from the session if it's there
    # session.pop('username', None)
    del session['user']
    return redirect('/')


@app.route('/build/<username>')
def build_new(username):
    """Build a new content."""

    # session["user"] = user.username
    user = crud.get_user_by_username(username)
    return render_template('build_your_own.html', user=user)
    
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

    flash("Your profile has been added")

    return redirect ('/')


@app.route('/add_comment', methods=['POST'])
def add_comment():
    """Add comment if user like to comment the content"""

    user_email = session.get("email")
    profile_id = request.form.get("profile_id")
    comment = request.form.get("comment")

    profile = crud.get_profile_by_profile_id(profile_id)
    add_comment = crud.create_comment(comment=comment, profile_id=profile_id)

    flash("Your Comment has been added")
    return redirect('/')


# @app.route('/')
# def add_like():
#     """Add like if user like the content"""

#     like = request.args.get("like")

#     return "You click like!"


# @app.route('/', methods=['POST'])
# def add_comment():
#     """Add comment if user like to comment the content"""

#     comment = request.form.get("comment")

#     return "You click comment!"



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)



# @app.route('/profile/view/<username>')
# def personal_profile(username):

    # username = crud.get_user_by_username(username)
    # user_id = get_user_by_username(username).user_id
    # # user_id = crud.get_user_by_username(username) # same as above

    # return render_template('homepage.html', user_id=user_id)


# @app.route('/profile/view/<username>')
# def view_personal_profile(username):

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

#     user_id = session.get("user_id")
#     # profile_id = request.form.get("profile_id")
#     comment = request.form.get("comment")

#     user_id = crud.get_user_by_id(user_id)
#     profile_id = crud.get_profile_by_id(profile_id)
#     add_comment = crud.create_comment(comment=comment, like=like, prodile_id=profile_id)

#     flash("Your Comment has been added")
#     return redirect('/')

# @app.route('/add_comment', methods=['POST'])
# def add_comment():
    # """User adding a comment to a profile"""

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

 



