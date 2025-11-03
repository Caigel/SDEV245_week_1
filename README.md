# Simple RBAC Demo (Authentication + Access Control)

This repo contains a minimal Python script showing:
- A simulated login with a hardcoded username and role
- Two roles: `admin` and `user`
- Two protected actions ("endpoints"): one admin-only, one user-only
- A public action for contrast
- A brief CIA triad explanation

## Outcomes Mapped
- *1.2:* Compare authentication vs. access control  
  - *Authentication* identifies **who** the user is (here, a hardcoded username read by `get_current_user()`).
  - *Access control (authorization)* determines **what** the user is allowed to do (enforced by `@role_required([...])`).
- *1.3:* Implement a basic access control mechanism  
  - Enforced via a decorator that checks the caller’s role before executing the action.

## Requirements Covered
- Login simulation: Hardcoded user/role; no password hashing or form input.
- Two roles: `admin` and `user`.
- Protected actions:  
  - `/admin-dashboard` (admin-only)  
  - `/user-portal` (user-only)

## Run It
```bash
python app.py
