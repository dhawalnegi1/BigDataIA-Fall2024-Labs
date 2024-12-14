from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta, timezone
import hmac, hashlib, jwt
from typing import Dict

SECRET_KEY = "abc"

def hash_password(password: str) -> str:
    secret_key = SECRET_KEY.encode()
    hash_object = hmac.new(secret_key, msg=password.encode(), digestmod=hashlib.sha256)
    hash_hex = hash_object.hexdigest()
    return hash_hex

def create_jwt_token(data: dict):
    expiration = datetime.now(timezone.utc) + timedelta(minutes=5)
    token_payload = {"exp": expiration, **data}
    token = jwt.encode(token_payload, SECRET_KEY, algorithm="HS256")
    return token, expiration

def decode_jwt_token(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_token
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

app = FastAPI()
security = HTTPBearer()

fake_users_db = {
    "demo": {
        "username": "demo",
        "email": "johndoe@example.com",
        "userid": 1,
        "hashed_password": hash_password("test"),
    }
}

def get_current_user(authorization: HTTPAuthorizationCredentials = Depends(security)):
    token = authorization.credentials
    try:
        payload = decode_jwt_token(token)
        username = payload.get("username")
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
                headers={"WWW-Authenticate": "Bearer"},
            )
        user = fake_users_db.get(username)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user
    except HTTPException as e:
        raise e

@app.post("/login")
def login(username: str, password: str):
    user = fake_users_db.get(username)
    if user and user["hashed_password"] == hash_password(password):
        token, expiration = create_jwt_token({"username": username})
        return {"access_token": token, "token_type": "bearer", "expires": expiration.isoformat()}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

@app.get("/protected")
def protected_route(current_user: Dict = Depends(get_current_user)):
    return {"message": f"Hello, {current_user['username']}!"}