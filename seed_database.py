"""Script to seed database."""

import os
import json
from random import choice, randint
# from datetime import datetime

import crud
import model
import server

os.system('dropdb profiles')
os.system('createdb profiles')

model.connect_to_db(server.app)
model.db.create_all()

# Load profile data from JSON file
# with open('data/profiles.json') as f:
#     profile_data = json.loads(f.read())

# Create profile, store them in list so we can use them
# to create fake comments
# profiles_in_db = []
# for profile in profile_data:
#     about, experience, skill, project, education, contact = (profile['about'],
#                                                              profile['experience'],
#                                                              profile['skill'],
#                                                              profile['project'],
#                                                              profile['education'],
#                                                              profile['contact'])
#     # release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

#     db_profile = crud.create_profile(about,
#                                      experience,
#                                      skill,
#                                      project,
#                                      education,
#                                      contact)
#     profiles_in_db.append(db_profile)

# Create 10 users; each user will make 10 ratings
# for n in range(10):
#     name = 'test'
#     email = f'user{n}@test.com'  # Voila! A unique email!
#     password = 'test'

#     user = crud.create_user(name, email, password)

#     for _ in range(10):
#         random_profile = choice(profiles_in_db)
#         like = randint(1, 5)

#         crud.create_comment(user, random_profile, like)