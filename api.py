from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json
from controllers import mainControllers
from database import db
from models import Organization

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/ey.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
CORS(app)
db.init_app(app)
# db.drop_all(app=app)
db.create_all(app=app)
api = Api(app)

api.add_resource(mainControllers.OrganizationList, '/orgs')
api.add_resource(mainControllers.OrganizationController, '/orgs/<org_id>')

api.add_resource(mainControllers.NewsController, '/news/<news_keyword>')

def populate_db():
  with app.app_context():
    o = Organization('Testing', '555-512-1234')
    db.session.add(Organization('Real Estate', '555-555-5555'))
    db.session.add(Organization('Insurance', '555-555-5556'))
    db.session.add(Organization('Private Equity', '555-555-5557'))
    db.session.commit()

# populate_db()

if __name__ == '__main__':
    app.run(debug=True)
