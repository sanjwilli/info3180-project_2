from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '$up3r$3cretkey'

UPLOAD_FOLDER = './app/static/imgs'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project2:mypassword@localhost/project2"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

from app import views