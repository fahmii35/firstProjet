from flask import Flask, request,redirect,url_for, render_template, flash,session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import LoginManager
from datetime import datetime
from sqlalchemy.sql import func
import os


# from flask_mail import Mail
# from flask_uploads import IMAGES , UploadSet , configure_uploads 





app=Flask(__name__)

app.secret_key='Sahlaneh secret-key'
app.config["SQLALCHEMY_DATABASE_URI"] =  "sqlite:///MyProject.db"



# flask upload configuration

# basedire = os.path.abspath(os.path.dirname(__file__))
# app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedire,'static/images')
# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)




# gmail configuration
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_USERNAME'] = 'sahlaneh1998@gmail.com'
# app.config['MAIL_PASSWORD'] = 'zeze nrrg sonw jntm'
# mail = Mail(app)

db=SQLAlchemy()
db.init_app(app)



login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))





class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    Nom = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200),  unique=True)
    password=db.Column(db.String(200), nullable=False)
   






   
with app.app_context():
    db.create_all()
