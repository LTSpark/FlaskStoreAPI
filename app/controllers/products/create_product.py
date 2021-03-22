from app.models.user import User
from app.models.category import Category
from app.models.product import Product

class CreateProduct:
    
    def __call__(self,request,category_name):

        if request.is_json:

            data = request.get_json()

            owner_email=data['owner_email']
            owner=User.get_by_email(owner_email)
            category=Category.get_by_name(category_name)

            if (owner and category):
                new_product=Product(
                    name=data['name'],
                    price=data['price'],
                    units=data['units'],
                    owner=owner,
                    category=category
                )
                
                return new_product.save()
                
            else:
                return {"message": "owner  or category doesn't exist"}   
        else:
            return {"error": "The request payload is not in JSON format"}