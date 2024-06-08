from fastapi import HTTPException, Request

from backend.domain.user import UserRole


class RBAC:
    def __init__(self, minimum_role: UserRole, auto_error: bool = True):
        super(RBAC, self).__init__()
        self._minimum_role: UserRole = minimum_role

    def __call__(self, request: Request):
        try:
            user_role = request.state.user.role
        except ValueError:
            raise HTTPException(status_code=403, detail="Invalid role")
        if user_role.value.hierarchy < self._minimum_role.value.hierarchy:
            raise HTTPException(
                status_code=403, detail="User does not have enough permissions."
            )
