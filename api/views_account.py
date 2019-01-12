def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': {
            "fullname": user.first_name + " " + user.last_name,
            "firstname": user.first_name,
            "lastname": user.last_name,
            "username": user.username
        }
    }



