from enum import Enum


class PlatformRole(str, Enum):
    ROLE_PLATFORM_USER: str = "ROLE_PLATFORM_USER"
    ROLE_PLATFORM_ADMIN: str = "ROLE_PLATFORM_ADMIN"