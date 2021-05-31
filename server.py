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

    return render_template('homepage.html')

# when user logout, redirect to homepage
@app.route('/', methods=['POST'])
def show_homepage():
    """View homepage."""

    return render_template('homepage.html')


# testing
@app.route('/bootstrap')
def show_bootstrap():
    """View homepage."""

    return render_template('bootstrap.html')



# Static Page (for demo)
@app.route("/Denise")
def user_profile():
    """Show particular user's profile"""

    return render_template("user_profile_page.html")

# Static Page (for demo)
@app.route("/Denise", methods=['POST'])
def show_user_profile():
    """Show particular user's profile"""

    return render_template("user_profile_page.html")


@app.route('/account')
def account_page():
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
        return redirect('/build/')

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
    
    del session['user']
    return redirect('/')


# when user sign in, username shows in url
@app.route('/build/<username>')
def build_new(username):
    """Build a new content."""

    user = crud.get_user_by_username(username)
    return render_template('build_your_own.html', user=user)
    

@app.route('/build')
def build_new_content():

    return redirect ('/build/<username>')


# for ajax submittion to homepage
# @app.route('/', methods=['POST'])
# def build_content():

#     about = request.form.get("about")
#     # experience = request.form.get("experience")
#     # project = request.form.get("project")
#     # skill = request.form.get("skill")
#     # education = request.form.get("education")
#     # contact = request.form.get("contact")

#     # return about, experience, project, skill, education, contact
#     return about


@app.route('/add_about', methods=['POST'])
def build_about_content():

    about = request.form.get("about")

    return about


@app.route('/add_experience', methods=['POST'])
def build_experience_content():

    experience = request.form.get("experience")

    return experience


@app.route('/add_project', methods=['POST'])
def build_project_content():

    project = request.form.get("project")

    return project


@app.route('/add_skill', methods=['POST'])
def build_skill_content():

    skill = request.form.get("skill")

    return skill


@app.route('/add_education', methods=['POST'])
def build_education_content():

    education = request.form.get("education")

    return education


@app.route('/add_contact', methods=['POST'])
def build_contact_content():

    contact = request.form.get("contact")

    return contact


@app.route('/add_comment', methods=['POST'])
def add_comment():
    """Add comment if user like to comment the content"""

    comment = request.form.get("comment")

    return comment



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)




# Query data from SQLAlchemy
# @app.route('/build', methods=['POST'])
# def build_new_content():

    # about = request.form.get("about") #dictionary key "about"
    # experience = request.form.get("experience")
    # project = request.form.get("project")
    # skill = request.form.get("skill")
    # education = request.form.get("education")
    # contact = request.form.get("contact")
    # user_id = session.get("user_id")

    # profile_content = crud.create_profile(about=about,
    #                               experience=experience,
    #                               skill=skill,
    #                               project=project,
    #                               education=education,
    #                               contact=contact,
    #                               user_id=user_id)

    # profile_about = crud.get_profile_by_about(about)
    # session["about"] = profile_about.about

    # profile_experience = crud.get_profile_by_experience(experience)
    # session["experience"] = profile_experience.experience

    # profile_project = crud.get_profile_by_project(project)
    # session["project"] = profile_project.project

    # profile_skill = crud.get_profile_by_skill(skill)
    # session["skill"] = profile_skill.skill

    # profile_education = crud.get_profile_by_education(education)
    # session["education"] = profile_education.education

    # profile_contact = crud.get_profile_by_contact(contact)
    # session["contact"] = profile_contact.contact

    # flash("Your profile has been added")

    # return redirect ('/build/<username>')

    






 



