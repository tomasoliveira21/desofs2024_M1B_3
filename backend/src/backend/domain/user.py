from enum import Enum
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, StringConstraints


class Role(BaseModel):
    name: Annotated[
        str,
        StringConstraints(
            min_length=1, max_length=24, to_lower=True, strip_whitespace=True
        ),
    ]
    hierarchy: Annotated[int, Field(ge=0)]


class DefaultRole(Role):
    def __init__(self, name="default", hierarchy=0):
        super().__init__(name=name, hierarchy=hierarchy)


class PremiumRole(Role):
    def __init__(self, name="premium", hierarchy=1):
        super().__init__(name=name, hierarchy=hierarchy)


class AdminRole(Role):
    def __init__(self, name="admin", hierarchy=2):
        super().__init__(name=name, hierarchy=hierarchy)


class UserRole(Enum):
    default = DefaultRole()
    premium = PremiumRole()
    admin = AdminRole()

    def __str__(self):
        return self.value.name

    @property
    def hierarchy(self):
        return self.value.hierarchy


class User(BaseModel):
    id: UUID
    email: EmailStr
    username: str
    role: UserRole
