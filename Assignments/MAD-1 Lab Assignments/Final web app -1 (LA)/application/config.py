import os

basedir=os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG=False
    SQLITE_DB_DIR=None
    SQLALCHEMY_DATABASE_URI=None
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class LocalDevelopmentConfig(Config):
    SQLITE_DB_DIR=os.path.join(basedir,"../db_directory")
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(SQLITE_DB_DIR,"db.sqlite3")
    DEBUG=True

'''
class ProductionDevelopmentConfig(Config):
    SQLITE_DB_DIR=os.path.join(basedir,"../db_directory")
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(SQLITE_DB_DIR,"proddb.sqlite3")
    DEBUG=False
    Password=os.getenv("PASSWORD") #it's bad to put psswords into the code, so do this
'''