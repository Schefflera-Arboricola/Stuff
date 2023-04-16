import os
from flask import Flask
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db


def create_app():
    app=Flask(__name__,template_folder="templates")
    if os.getenv('ENV',"development")=="production": 
        #if no value setup for ENV variable then it will setup to "development"
        raise Exception("Currently no production config is setup.")
    else:
        print("Starting Local Development")
        app.config.from_object(LocalDevelopmentConfig)
    
    db.init_app(app)
    app.app_context().push()
    return app

app=create_app()

from application.controllers import main
app.register_blueprint(main)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port=8080)
    

