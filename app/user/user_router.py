from flask import request

from . import user_bp

from app.controllers.user.create_user import CreateUser
from app.controllers.user.get_users import GetUsers
from app.controllers.user.get_user import GetUser

@user_bp.route("/user", methods=["POST"])
def post_user():  
    create_user=CreateUser()
    return create_user(request)


@user_bp.route("/users", methods=["GET"])
def get_users():
    get_users=GetUsers()
    return get_users()

@user_bp.route("/user/<user_name>", methods=["GET"])
def get_user(user_name):
    get_user=GetUser()
    return get_user(user_name)

'''
@user_bp.route("/users/email", methods=["GET"])
def get_user_email():

    email=request.json['email']
    user=User.get_by_email(email)

    if not user:
        return {"msg": f"couldn't found {email}"}

    return {
        "id": f"{user.id}",
        "name": f"{user.name}",
        "email": f"{user.email}"
    }

@user_bp.route("/users/like", methods=["GET"])
def get_like_users():

    name=request.json['name']
    users=User.get_like_user(name)

    if not users:
        return {"msg": f"couldn't found {name}"}
    print(users)
    return { 
        "name": f"printed in console"
    }

@user_bp.route("/users/paginate/<int:page_num>", methods=["GET"])
def get_paginated_users(page_num):

    pagination= User.query.filter_by(active=True).order_by(User.id).paginate(per_page=2, page=page_num, error_out=True)
    for i in range(pagination.pages):
        print(pagination.items)
        pagination=pagination.next()
 
    return {"msg": "printed in console"}
'''


     

        


