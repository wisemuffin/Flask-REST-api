import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    # parsing ensure only the correct data gets to your endpoints
    parser = reqparse.RequestParser()  # ensure only certain parts of the payload are passed into data
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field can not be blank'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field can not be blank'
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):  # can ommit is not None
            return {'message': 'user already exists'}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "user created successefully"}, 201
