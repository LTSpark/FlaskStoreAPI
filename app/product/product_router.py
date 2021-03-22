from flask import request

from . import  product_bp
from app.controllers.products.create_product import CreateProduct
from app.controllers.products.get_products import GetProducts
from app.controllers.products.get_products_by_category import GetProductsByCategory

@product_bp.route("/product/<category_name>", methods=["POST"])
def post_product(category_name):
    create_product=CreateProduct()
    return create_product(request,category_name)

@product_bp.route("/products",methods=["GET"])
def get_products():
    get_products=GetProducts()
    return get_products()

@product_bp.route("/products/<category_name>",methods=["GET"])
def get_products_by_category(category_name):
    get_products_by_category=GetProductsByCategory()
    return get_products_by_category(category_name)


'''
@product_bp.route("/products/user",methods=["GET"])
def get_products_user():
    email=request.json['email']
    products=User.get_products_by_user(email)
    for i in range(len(products)):
        print(products[i])
    return {"msg": "printed in console"}

@product_bp.route("/products/user/join",methods=["GET"])
def get_products_join():
    results=Product.join_user()
    for result in results:
        print(result)
    return {"msg": "printed in console"}
'''