from sqlalchemy.exc import IntegrityError
from marshmallow import fields

from app import db, ma

from utils.validators import validate_product

class Product(db.Model):
    
    __tablename__='products'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    price=db.Column(db.Float,nullable=False)
    units=db.Column(db.Integer,nullable=False)

    owner_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    category_id=db.Column(db.Integer,db.ForeignKey('categories.id'))

    def __repr__(self):
        return f'{self.id}) {self.name}: ${self.price} - {self.units} unit(s)'
    
    def save(self):
        if validate_product(self.name,self.price,self.units):
            try:
                db.session.add(self)    
                db.session.commit()
                return {"message": f"product {self.name} has been created successfully."}
            except IntegrityError as e:
                db.session.rollback()
                return {
                    "message": f"product {self.name} couldn't be created",
                    "errors": e
                    }
        else:
            {"message": f"product {self.name} could not be created"}
    
    @staticmethod
    def get_products_by_category(Category,User,category_name):
        products=Product.query.filter(Category.name==category_name,User.active==True)\
                    .join(User).join(Category)
        return products