from functools import wraps
from flask import request
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from werkzeug.exceptions import Unauthorized


def authMiddleware():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            from ...infrastructure import UserDataModel
            verify_jwt_in_request()
            claims = get_jwt()

            if claims['sub'] is None:
                raise Unauthorized(description={'msg': 'Not Authorized'},
                                   response={'msg': 'Not Authorized'})
            user = UserDataModel.query.filter_by(id=claims['sub']).first()
            request.user = user.to_json()
            return fn(*args, **kwargs)
        return decorator
    return wrapper
