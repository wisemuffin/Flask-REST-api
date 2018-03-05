from flask import Flask
from flask_restful import Api
from flask_jwt import JWT  # jason web token, and a decorator for JWT
import datetime

from security import authenticate, identity  # im the same folder
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
# sqllite db exists in the root folder. This could be mysql or oracle or postgress or any other db :)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'dave@whatgogu15bonus65fgfdn'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()  # creates based on SQLALCHEMY_DATABASE_URI


jwt = JWT(app, authenticate, identity)  # creates a new endpoint /auth

# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=1800)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
