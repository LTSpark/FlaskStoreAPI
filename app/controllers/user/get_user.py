from flask import jsonify
from app import ma
from app.models.user import User
from app.models.schemas import UserSchema

class GetUser:
    def __call__(self,name_user):
        query_user=User.query.filter_by(active=True,name=name_user).first()
        user_schema=UserSchema()
        user=user_schema.dump(query_user)
        return jsonify({'users': user})