from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from utils.validators import validate_category
from marshmallow import fields

from app import db, ma

class Category(db.Model):
    
    __tablename__='categories'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False,unique=True)

    products=db.relationship('Product',backref='category',cascade='all, delete, delete-orphan',lazy='dynamic')
        
    def __repr__(self):
        return f'{self.id}) {self.name}'
    
    def save(self):
        if validate_category(self.name):
            try:
                db.session.add(self)
                db.session.commit()
                return True
            except IntegrityError as e:
                print(e)
                db.session.rollback()
                return False
        else:
            return False

    @staticmethod
    def get_categories():
        categories=Category.query.filter().order_by(Category.id).all()
        return categories
    
    @staticmethod
    def get_product_categories(Product):
        categories=db.session.query(Category).join(Product).group_by(Category.id)
        return categories
    
    @staticmethod
    def get_subtotal_costs_category(Product):
        subtotals=db.session.query(Category.id,Category.name,func.sum(Product.price*Product.units))\
                    .join(Product).group_by(Category.id).all()
        return subtotals
    
    def get_by_name(name):
        category=Category.query.filter(Category.name==name).first()
        return category