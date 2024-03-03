from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session

from database import SessionLocal
from fastapi import HTTPException, Depends, status, Security
from jose import JWTError
from datetime import datetime, timedelta
import jwt
from fastapi import FastAPI, Header, HTTPException

from register_login.model import User





def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Exemple basique d'un middleware d'authentification
SECRET_KEY = "votre_secret_jwt"
ALGORITHM = "HS256"

api_key_header = APIKeyHeader(name="Authorization", auto_error=True)

def get_api_key(api_key: str = Security(api_key_header)):
    """
    Extrait et valide le préfixe du token JWT dans l'en-tête Authorization.
    """
    if api_key is None:
        raise HTTPException(status_code=403, detail="Token d'authentification non fourni")
    return api_key

def verify_token(api_key: str = Depends(get_api_key)):
    """
    Valide le format et la signature du token JWT.
    """
    token_prefix = "Bearer "
    if not api_key.startswith(token_prefix):
        raise HTTPException(status_code=403, detail="Token mal formaté, préfixe 'Bearer ' attendu")
    token = api_key[len(token_prefix):]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # Vous pouvez retourner un modèle d'utilisateur basé sur le payload si nécessaire
    except jwt.PyJWTError as e:
        raise HTTPException(status_code=403, detail="Token invalide ou expiré.") from e


def get_token_from_header(authorization: str = Header(None)):
    """
    Extrait le token JWT de l'en-tête Authorization.
    """
    token_prefix = "Bearer "
    if authorization is None or not authorization.startswith(token_prefix):
        raise HTTPException(status_code=403, detail="Token d'authentification non fourni ou mal formaté.")
    return authorization[len(token_prefix):]

def get_user_from_token(token: str):
    """
    Valide le token JWT.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub", None)  # Ou retournez un modèle d'utilisateur basé sur le payload si nécessaire
    except jwt.PyJWTError as e:
        raise HTTPException(status_code=403, detail="Token invalide ou expiré.") from e

# def get_user(user_id: int, db: Session):
#     return db.query(User).filter(User.id == user_id).first()

# async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         user_id: int = int(payload.get("sub"))
#         if user_id is None:
#             raise credentials_exception
#         user = get_user(user_id, db)
#         if user is None:
#             raise credentials_exception
#         return user
#     except JWTError:
#         raise credentials_exception



# Fonction pour créer un token JWT
def create_jwt_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15) # Expiration par défaut de 15 minutes
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Fonction pour décoder un token JWT
def decode_jwt_token(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token
    except jwt.ExpiredSignatureError:
        # Gérer l'expiration du token
        return {"message": "Token expired"}
    except jwt.InvalidTokenError:
        # Gérer le token invalide
        return {"message": "Invalid token"}