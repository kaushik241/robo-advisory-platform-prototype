#puppy company blgo __init__.py 
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager




app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'
######################
###DataBase Setup#####
######################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'


db = SQLAlchemy(app)
Migrate(app,db)


#######Login Configs########
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'


##########################


 
from robo.core.views import core
from robo.users.views import users
#from puppycompanyblog.blog_posts.views import blog_posts
from robo.error_pages.handlers import error_pages
from robo.calculator.views import calculator
from robo.quiz.views import quiz




app.register_blueprint(core)
app.register_blueprint(users)
#app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)
app.register_blueprint(calculator)
app.register_blueprint(quiz)
