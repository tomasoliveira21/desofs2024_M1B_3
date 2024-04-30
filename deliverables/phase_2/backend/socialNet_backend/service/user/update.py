from socialNet_backend.app import config
from socialNet_backend.db.repository import user_repo
from socialNet_backend.service.authentication.password import hash_password, check_password_strength
from socialnet.lib.dates import utcnow


def update_user_password(user, password):
    if config.REQUIRE_STRONG_PASSWORDS:
        check_password_strength(password)

    password_hash = hash_password(password)
    user_repo.update_user(user, password=password_hash, password_updated_at=utcnow())
    return user
