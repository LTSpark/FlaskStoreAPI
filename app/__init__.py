import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from dotenv import load_dotenv


db=SQLAlchemy()
ma = Marshmallow()

def create_app():

    app=Flask(__name__)

    load_dotenv()
    
    app.config['SQLALCHEMY_DATABASE_URI']=os.getenv("DATABASE")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['DEBUG']=True
    
    db.init_app(app)
    ma.init_app(app)

    migrate=Migrate(app,db)
    manager=Manager(app)

    from .user import user_bp
    app.register_blueprint(user_bp)

    from .product import product_bp
    app.register_blueprint(product_bp)

    from .category import category_bp
    app.register_blueprint(category_bp)
 
    migrate.init_app(app,db)
    manager.add_command('db',MigrateCommand)

    return manager