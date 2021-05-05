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

    return render_template('homepage.html')



@app.route('/build')
def build_new():
    """Build a new content."""

    # username = session.get("username")
    # username = "Denise"
    user = crud.get_users()
    # user = crud.get_user_by_username(username)
    # content = "about something"
    # content = session.get("content")

    return render_template('build_your_own.html', user=user)



@app.route('/build/<int:user_id>')
def show_content(user_id):

    user_id = crud.get_user_by_id(user_id)
    # username = User.query.filter(User.username == username).first()

    return render_template('build_your_own.html', user_id=user_id)


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
    user_id = session.get("user_id")

    profile = crud.create_profile(about=about,
                                  experience=experience,
                                  skill=skill,
                                  project=project,
                                  education=education,
                                  contact=contact,
                                  user_id=user_id)
    
    # all_contents = crud.get_profile_contents()
    
    # result = list()
    # for content in profile:
    #     profile = crud.create_profile(about=about,
    #                                     experience=experience,
    #                                     skill=skill,
    #                                     project=project,
    #                                     education=education,
    #                                     contact=contact,
    #                                     user_id=user_id)
    #     result.append({
    #         "about": about,
    #         "experience": experience,
    #         "skill": skill,
    #         "project": project,
    #         "education": education,
    #         "contact": contact,
    #         # "user_id": user_id
    #     })
    
    flash("Your profile has been added")
    return render_template('build_your_own.html')
    # return render_template('build_your_own.html', result=result)
    


@app.route('/account')
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template('account.html', users=users)

# @app.route('/users/<user_id>')
# def user_details(user_id):
#     """View user details."""

#     user = crud.get_user_by_id(user_id)

#     return render_template('account.html', user=user)


@app.route('/account', methods=['POST'])
def register_users():
    """Create a new user."""

    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # user = crud.get_user_by_email(email)
    user = crud.get_user_by_username(username)


    if user:
        flash('Email has already taken. Try again')
        
        return redirect('/account')

   
    else:
        crud.create_user(username, email, password)
        flash('Your account has been created.')

        return redirect('/build')


@app.route('/login', methods=['POST'])
def user_login():
    """Login user"""

    input_email = request.form.get('email')
    input_password = request.form.get('password')

    user = crud.get_user_by_email(input_email)


    if user and user.password == input_password:
        session['user'] = user.user_id
        flash('Logged in.')
        return redirect('/build')
    
   
    else:
        flash('incorrect login')
        return redirect('/users')


# @app.route("/add_comment", methods=['POST'])
# def add_comment():
#     """User adding a comment to a profile"""

#     user_id = session.get("user_id")
#     profile_id = request.form.get("profile_id")
#     comment = request.form.get("comment")


#     profile = crud.get_blog_by_id(profile_id)

#     add_comment = crud.create_comment(comment=comment, like=like, prodile_id=profile_id)

#     flash("Your Comment has been added")

#     return redirect('/build')
    # return redirect('/build/<username>')


# @app.route("/add_like", methods=['POST'])
# def add_comment():
#     """User adding a like to a profile"""

#     user_id = session.get("user_id")
#     profile_id = request.form.get("profile_id")
#     like = request.form.get("like")

#     profile = crud.get_blog_by_id(profile_id)

#     add_like = crud.create_comment(comment=comment, like=like, prodile_id=profile_id)

#     flash("You like it")

#     return redirect('/build')
    # return redirect('/build/<username>')
 




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)