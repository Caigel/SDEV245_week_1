"""
Simple authentication + role-based access control (RBAC) demo.
Requirements satisfied:
- Hardcoded username and role (no password hashing or form input)
- Two roles: admin and user
- Two protected actions: one admin-only, one user-only
- Short CIA triad explanation at bottom (Confidentiality)
"""

from functools import wraps

# --- "Database": hardcoded users and roles ---
USERS = {
    "alice": {"role": "admin"},
    "bob":   {"role": "user"},
}

# --- Simulated login (pick a username to "log in") ---
# Change this to "alice" or "bob" to see different access results.
CURRENT_USERNAME = "alice"   # try "bob" as well

def get_current_user():
    """Return the current user's identity and role from the hardcoded store."""
    user = USERS.get(CURRENT_USERNAME)
    if not user:
        raise ValueError(f"Unknown user: {CURRENT_USERNAME}")
    return {"username": CURRENT_USERNAME, "role": user["role"]}

# --- Access control decorator ---
def role_required(allowed_roles):
    """
    Decorator to enforce role-based access to a function.
    Usage: @role_required(["admin"])  -> admin-only
           @role_required(["user"])   -> user-only
    """
    def _decorator(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            user = get_current_user()
            if user["role"] not in allowed_roles:
                raise PermissionError(
                    f"Access denied: '{user['username']}' (role={user['role']}) "
                    f"cannot call '{func.__name__}' (allowed roles: {allowed_roles})."
                )
            return func(*args, **kwargs)
        return _wrapper
    return _decorator

# --- Protected actions ("endpoints") ---
@role_required(["admin"])
def view_admin_dashboard():
    return "Admin dashboard: system metrics, user management, and audit logs."

@role_required(["user"])
def view_user_portal():
    return "User portal: your profile, recent activity, and personal settings."

# --- Public action (no protection, just for contrast) ---
def view_homepage():
    return "Welcome! This is a public homepage anyone can see."

# --- Demo runner ---
def main():
    user = get_current_user()
    print(f"Logged in as: {user['username']}  (role={user['role']})")
    print()

    # Public route
    print("[PUBLIC]  /homepage")
    print(" ->", view_homepage())
    print()

    # User-only route
    print("[USER]    /user-portal")
    try:
        print(" ->", view_user_portal())
    except PermissionError as e:
        print(" ->", e)
    print()

    # Admin-only route
    print("[ADMIN]   /admin-dashboard")
    try:
        print(" ->", view_admin_dashboard())
    except PermissionError as e:
        print(" ->", e)
    print()

    # Quick switch demo: toggle CURRENT_USERNAME and re-run to compare.
    print("Tip: Change CURRENT_USERNAME to 'bob' to see access differences.")

if __name__ == "__main__":
    main()

"""
CIA Triad note (Confidentiality):
This script demonstrates Confidentiality by restricting information based on role.
Only admins can read the admin dashboard; only regular users can view the user portal.
Unauthorized principals receive an explicit denial (PermissionError), preventing disclosure.
"""
