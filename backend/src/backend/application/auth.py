from time import time

import jwt
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from backend.infrastructure.config import settings
from supabase import create_client


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials | None = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )
            if not self.verify_supabase_session(jwtoken=credentials.credentials):
                raise HTTPException(status_code=403, detail="User not found.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_supabase_session(self, jwtoken: str) -> bool:
        try:
            client = create_client(
                supabase_url=settings.supabase_auth_url,
                supabase_key=settings.supabase_auth_key,
            )
            client.auth.get_user(jwtoken)
            return True
        except Exception:
            return False

    def decode_jwt(self, jwtoken: str) -> dict | Exception:
        try:
            decoded_token = jwt.decode(
                jwt=jwtoken,
                key=settings.jwt_secret_key,
                algorithms=settings.jwt_algorithms,
                audience=settings.jwt_audience,
            )
            print(f"token={decoded_token}")
            if decoded_token["exp"] >= time():
                return decoded_token
            else:
                raise Exception("Expired JWT Token")
        except Exception as e:
            raise e

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = True
        try:
            self.decode_jwt(jwtoken=jwtoken)
        except Exception:
            isTokenValid = False
        return isTokenValid
