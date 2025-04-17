import base64
from functools import wraps
from flask import request, jsonify
from repo.user import find_user_by_email


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({
                "success": False,
                "message": "Authentication required. Please provide a valid token."
            }), 401
            
        if not auth_header.startswith('Bearer '):
            return jsonify({
                "success": False,
                "message": "Invalid token format or there is no token. Use 'Bearer <token>'"
            }), 401
            
        try:
            token = auth_header.split(' ')[1]
            user = claim_user(token)
            if not user:
                return jsonify({
                    "success": False,
                    "message": "Invalid or expired token"
                }), 401
                
            request.user = user
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({
                "success": False,
                "message": "Authentication failed. Please login again."
            }), 401
            
    return decorated_function

def claim_user(token):
    try:
        user_data = base64.b64decode(token).decode().split(":")
        email = user_data[0]
        user = find_user_by_email(email)
        
        if not user:
            return None
            
        user_dict = user.obj_to_dict()
        user_dict.pop('user_password', None)
        return user_dict
        
    except Exception:
        return None

def get_token(user):
    email = user.user_email
    user_id = user.user_id
    return base64.b64encode(f"{email}:{user_id}".encode()).decode()
