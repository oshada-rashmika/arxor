try:
    from models.customer_profile import CustomerProfile
    from models.user import User, UserRole, user_role_enum
except ImportError:
    from backend.models.customer_profile import CustomerProfile
    from backend.models.user import User, UserRole, user_role_enum

__all__ = ["User", "UserRole", "user_role_enum", "CustomerProfile"]
