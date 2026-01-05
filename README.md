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

## Template Syntax and Debugging

### What I Learned

**Django Template Syntax**
- Correct template tag syntax uses `{% %}` for logic and `{{ }}` for variables
- Common tags: `{% extends %}`, `{% block %}`, `{% endblock %}`, `{% csrf_token %}`

```django
<!-- Correct -->
{% block content %}
{% endblock %}

<!-- Incorrect -->
{<% block content %>}
{<% endblock %>}
```

**Template Error Debugging**
| Error Type | Symptom | Solution |
|------------|---------|----------|
| `TemplateSyntaxError: Unclosed tag` | Server returns 500 error | Check all `{% block %}` have matching `{% endblock %}` |
| Incorrect delimiter | Template not rendering | Replace `{<% %>}` with `{% %}` |
| Encoding issues | Character display problems | Use `charset="utf-8"` (not `uft-8`) |

**Code Consistency**
- Maintain consistent indentation (4 spaces per level in HTML/Django templates)
- Fix syntax errors in base templates first (they cascade to child templates)

### Challenges Encountered

**1. Template Delimiter Confusion**
**Problem**: Mixed up template syntax delimiters `{<% %>}` instead of `{% %}`
```django
<!-- Wrong -->
{<% block content %>}
{<% endblock %>}
```

**Solution**: Use correct Django template syntax
```django
<!-- Correct -->
{% block content %}
{% endblock %}
```

**2. Cascading Template Errors**
**Problem**: Errors in `base.html` affected all pages extending it
- Fixed `base.html` first (parent template)
- Then fixed `index.html` (child template)

**3. Character Encoding Typo**
**Problem**: `charset="uft-8"` caused potential encoding issues

**Solution**: Corrected to `charset="utf-8"`

---

### Session Notes
Fixed Django template syntax errors across multiple files. Corrected delimiter syntax from `{<% %>}` to `{% %}` in both base.html and index.html templates. Also fixed character encoding typo (`uft-8` → `utf-8`) and normalized HTML indentation. Template inheritance errors in parent templates cascade to all child templates, requiring systematic debugging from base templates first.
