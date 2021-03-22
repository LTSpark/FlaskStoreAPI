from flask import jsonify

from app.models.user import User
from app.models.product import Product
from app.models.category import Category
from app.models.schemas import ProductSchema

class GetProductsByCategory:

    def __call__(self,category_name):
        query_products=Product.get_products_by_category(Category,User,category_name)
        product_schema=ProductSchema(many=True,exclude=("category",))
        products_by_category=product_schema.dump(query_products)
        return jsonify({"Products": products_by_category})