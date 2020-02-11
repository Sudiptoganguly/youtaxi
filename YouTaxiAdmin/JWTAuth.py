import jwt


def Encode(payload):
    jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
    print("Token : ", jwt_token['token'].decode("utf-8"))
    return jwt_token['token'].decode("utf-8")

def Decode():
    pass
