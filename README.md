# Django Job Application Project

## Setup

### 1. Install Dependencies
```bash
pip install python-dotenv
```

### 2. Configure Environment Variables
Copy `.env.example` and fill in your values:
```bash
cp .env.example .env
```

Required variables in `.env`:
```
SECRET_KEY=
EMAIL_BACKEND=
EMAIL_HOST=
EMAIL_PORT=
EMAIL_USE_TLS=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```

**Note**: Use quotes for values containing `#` or special characters.

**Gmail**: Generate an [App Password](https://support.google.com/accounts/answer/185833) (requires 2FA).

### 3. Run Server
```bash
python manage.py runserver
```

## Key Settings

| Setting | Description | Location |
|---------|-------------|----------|
| `DEFAULT_AUTO_FIELD` | Default primary key type for models | `settings.py` (not `.env`) |
| `SECRET_KEY` | Django security key | `.env` (required) |
| Email settings | SMTP configuration | `.env` (loaded dynamically) |

## What I Learned

### Environment Variable Management
- **Security**: Keep secrets out of version control using `.env` (gitignored)
- **`.env.example`**: Template file for other developers (safe to commit)
- **Strict mode**: Raise error if `SECRET_KEY` is missing

```python
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("SECRET_KEY must be set in .env file")
```

### Django Email Configuration
- **Dynamic backends**: Switch between `console` (dev) and `smtp` (prod)
- **Type conversion**: Environment variables are strings by default

```python
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True"
```

### Best Practices
| What | Why |
|------|-----|
| Environment variables for secrets | Prevents credential leaks in Git |
| Quote special characters in `.env` | Avoid `#` being treated as comment |
| Explicit error handling | Fail fast if config is missing |

## Challenges

### 1. Comment Character Issue
**Problem**: If `SECRET_KEY` contains `#`, `.env` treats everything after it as a comment.
```
SECRET_KEY=~~~~~#~~
```

**Solution**: Use quotes to preserve the entire value.
```
SECRET_KEY="~~~~~#~~"
```

### 2. Type Conversion
**Problem**: Environment variables are always strings.

**Solution**: Convert explicitly.
```python
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))  # string → int
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True"  # string → bool
```

### 3. Deciding What to Externalize
| Setting | Externalize? | Reason |
|---------|--------------|--------|
| `SECRET_KEY` | Yes | Sensitive credential |
| `EMAIL_HOST_PASSWORD` | Yes | Sensitive credential |
| `EMAIL_BACKEND` | Yes | Environment-specific (dev vs prod) |
| `EMAIL_HOST` | Yes | Flexibility (different services) |
| `EMAIL_PORT` | Yes | Service-specific configuration |
| `DEFAULT_AUTO_FIELD` | No | Static Django setting |
