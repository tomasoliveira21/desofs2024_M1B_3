from time import time

import jwt
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from backend.infrastructure.config import settings
from backend.service.user_service import UserService


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
            else:
                request.state.jwt = credentials.credentials

            try:
                decoded_token = jwt.decode(
                    jwt=request.state.jwt,
                    key=settings.jwt_secret_key,
                    algorithms=settings.jwt_algorithms,
                    audience=settings.jwt_audience,
                )
                request.state.credentials = decoded_token
            except Exception:
                raise HTTPException(
                    status_code=500, detail="Could not decode JWT Token."
                )

            if not request.state.credentials["exp"] >= time():
                raise HTTPException(status_code=403, detail="JWT Token has expired.")

            try:
                request.state.user = UserService().get_self_user(request=request)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

            return credentials.credentials
