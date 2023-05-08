from dotenv import load_dotenv
import os


load_dotenv()

UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

SECRET_KEY = os.environ.get('SECRET_KEY')
