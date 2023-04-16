from flask_restful import Resource
from application.models import *
from flask_restful import fields, marshal_with, reqparse
from application.database import db
from application.models import User
from application.validation import NotFoundError, BusinessValidationError

output_fields={"user_id":fields.Integer,"username": fields.String,"email": fields.String}
create_user_parser=reqparse.RequestParser()
create_user_parser.add_argument('username')
create_user_parser.add_argument('email')

class UserAPI(Resource):
    @marshal_with(output_fields)
    def get(self, username):
        print("In UserAPI GET Method", username)
        user=db.session.query(User).filter(User.username==username).first()
        if user :
            return user
        else:
            raise NotFoundError("User not found") 
        #why everyone calls dictionary a JSON file?
    
    def put(self, username):
        print("PUT username : ",username) 
        return {"username":username}
    
    def delete(self, username):
        print("DELETE username : ",username)
        return {"username":username,"action":"DELETE"}
    
    def post(self):
        args=create_user_parser.parse_args()
        username=args.get('username',None)
        email=args.get('email',None)
        if username is None:
            raise BusinessValidationError(status_code=400,error_code="BE1001",error_message="Username is mandatory")
        if email is None:
            raise BusinessValidationError(status_code=400,error_code="BE1002",error_message="Email is mandatory")
        user=db.session.query(User).filter((User).filter((User.username==username) | (User.email==email))).first()
        
        if user:
            raise BusinessValidationError(status_code=400,error_code="BE1003",error_message="User already exists")
        
        new_user=User(username=username,email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user, 201

