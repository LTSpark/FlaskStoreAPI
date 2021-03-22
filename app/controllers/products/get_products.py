from flask import jsonify

from app.models.category import Category
from app.models.product import Product
from app.models.user import User
from app.models.schemas import AllCategoryProductsSchema

'''
We first get categories because we want to 
send products ordered by their categories:
that's why we don't query product but category
'''

class GetProducts:
    def __call__(self):

        query_categories=Category.get_product_categories(Product)
        product_category_schema=AllCategoryProductsSchema(many=True)
        products=product_category_schema.dump(query_categories)

        return jsonify({'Products': products})