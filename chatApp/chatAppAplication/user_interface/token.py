import datetime
import jwt
from chatAppAplication.settings import SECRET_KEY

def token_activation(username, password):
    data = {
        'username': username,
        'password': password,
        'exp': datetime.datetime.now()+datetime.timedelta(minutes=6)
    }

    token = jwt.encode(data, SECRET_KEY, algorithm="HS256").decode('utf-8')

    return token
