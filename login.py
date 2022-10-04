from flask import Blueprint
from flask import request
from flask_jwt_extended import create_access_token
import response as resp
from response import response_with
from model import Users, db
from passlib.hash import pbkdf2_sha1 as sha1

login_routes = Blueprint("login_routes", __name__)


@login_routes.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        hashed_password = sha1.hash(data.get('password'))
        new_user = Users(username=data.get('username'), password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return response_with(resp.SUCCESS_201)
    except Exception as error:
        print(error)
        return response_with(resp.INVALID_INPUT_422)


@login_routes.route('/login', methods=['POST'])
def login_authenticate():
    try:
        data = request.get_json()
        username_get = data.get('username')
        current_user = Users.query.filter(Users.username == username_get).first()
        if not current_user:
            return resp.response_with(resp.SERVER_ERROR_404)
        if Users.verify_hash(data.get('password'), current_user.password):
            access_token = create_access_token(identity=data.get('username'))
            return response_with(resp.SUCCESS_201,
                                 value={'message': 'Logged in as {}'.format(current_user.username),
                                        "access_token": access_token})
        else:
            return resp.response_with(resp.UNAUTHORIZED_403)
    except Exception as error:
        print(error)
        return response_with(resp.INVALID_INPUT_422)


        return data
    except Exception as error:
        print(error)
        return response_with(resp.INVALID_INPUT_422)
