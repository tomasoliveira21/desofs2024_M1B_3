from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer

from backend.domain.user import UserRole


class RBAC(HTTPBearer):
    def __init__(self, minimum_role: UserRole, auto_error: bool = True):
        super(RBAC, self).__init__(auto_error=auto_error)
        self._minimum_role: UserRole = minimum_role

    async def __call__(self, request: Request):
        await super(RBAC, self).__call__(request)
        try:
            user_role = UserRole[request.state.role]
        except ValueError:
            raise HTTPException(status_code=403, detail="Invalid role")
        if user_role.value.hierarchy < self._minimum_role.value.hierarchy:
            raise HTTPException(
                status_code=403, detail="User does not have enough permissions."
            )
