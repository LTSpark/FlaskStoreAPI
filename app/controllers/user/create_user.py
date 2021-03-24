from app.models.user import User

class CreateUser():

    def __call__(self,request):


        if request.is_json:
            data=request.get_json()
            age=data['age']
            job=data['job']
            city=data['city']
            gender=data['gender']

            new_user=User(
                name=data['name'],
                email=data['email'],
                active= True,
                role=data['role'],
                password=data['password']
            )

            if new_user.save(age,job,city,gender):      
                return {"message": f"user {new_user.name} has been created successfully."}
            else:
                return {"message": f"user {new_user.name} could not be created"}
        else:
            return {"error": "The request payload is not in JSON format"}
