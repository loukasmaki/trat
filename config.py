import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "Shh-a-secret-secret-key-dont-tell"
    db_user = "db_user"
    db_password = "password"
    db_host = "localhost"
    db_port = "5432"
    db_name = "trat"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    weapon_class_list = [
        ('Brottning', 'Brottning'),
        ('Långsvärd Grundkurs', 'Långsvärd Grundkurs'),
        ('Långsvärd Fortsättning', 'Långsvärd Fortsättning'),
        ('Sabel', 'Sabel'),
        ('Rapir & Dolk', 'Rapir & Dolk'),
        ('Svärd & Bucklare', 'Svärd & Bucklare'),
        ('Barn & Ungdom', 'Barn & Ungdom')
    ]


