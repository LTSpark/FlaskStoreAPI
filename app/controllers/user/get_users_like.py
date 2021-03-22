from flask import jsonify

from app.models.user import User
from app.models.schemas import UserSchema

class GetUsersLike:
    def __call__(self,user_name):
        query_user=User.get_users_like(user_name)
        user_schema=UserSchema(many=True)
        user=user_schema.dump(query_user)
        return jsonify({'users': user})