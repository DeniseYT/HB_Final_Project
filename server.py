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

    if 'username' in session:
        username = session['username'] 

    return render_template('homepage.html')


@app.route('/build')
def build_new():
    """Build a new content."""

    return render_template('build_your_own.html')

# # for showing on url
# @app.route('/build/<username>')
# def show_username(username):
#     """Show username in url""" 
    
#     username = crud.get_user_by_username(username)

#     return redirect('/build')

# for showing on url
# having issue
# @app.route('/get-username', methods=['GET'])
# def get_name():
#     """Get username from session."""

#     username = request.args.get("username")
#     session["username"] = "username"
    
#     return redirect("/")



@app.route('/build', methods=['POST'])
def build_new_content():
    """User build their own content."""

    about = request.form.get("about")
    experience = request.form.get("experience")
    project = request.form.get("project")
    skill = request.form.get("skill")
    education = request.form.get("education")
    contact = request.form.get("contact")

    profile = crud.create_profile(about=about,
                                  experience=experience,
                                  skill=skill,
                                  project=project,
                                  education=education,
                                  contact=contact)
    
    flash("Your profile has been added")
    # flash("Your profile has been added", profile=profile)

    return redirect("/build")




@app.route('/users')
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template('account.html', users=users)

# @app.route('/users/<user_id>')
# def user_details(user_id):
#     """View user details."""

#     user = crud.get_user_by_id(user_id)

#     return render_template('account.html', user=user)


@app.route('/users', methods=['POST'])
def register_users():
    """Create a new user."""

    email = request.form.get('email')
    password = request.form.get('password')

    # flash not shows up
    if crud.get_user_by_email(email) == email:
        flash('You can’t create an account with that email. Try again')

    # working fine
    else:
        crud.create_user(email, password)
        flash('Your account has been created.')

    return redirect('/build')


@app.route('/login', methods=['POST'])
def user_login():
    """Login user"""

    input_email = request.form.get('email')
    input_password = request.form.get('password')

    user = get_user_by_email(input_email)

    # working fine
    if user and user.password == input_password:
        session['user'] = user.user_id
        flash('Logged in.')
        return redirect('/build')
    
    # working fine
    else:
        flash('incorrect login')
        return redirect('/users')


    




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)