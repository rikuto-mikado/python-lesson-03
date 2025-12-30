# Django Job Application Project

## Initial Setup

### 1. Environment Variables

This project uses environment variables to manage sensitive information. Follow these steps:

1. Copy `.env.example` to create your own `.env` file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your actual values:
   ```
   SECRET_KEY=your-secret-key-here
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-gmail-app-password
   ```

**Note**: For Gmail, you need to generate an [App Password](https://support.google.com/accounts/answer/185833) (requires 2-factor authentication enabled).

### 2. Install Dependencies

```bash
pip install python-dotenv
```

### 3. Additional Notes

**Environment Variables in settings.py**: SECRET_KEY and email credentials are loaded from `.env` to avoid exposing sensitive data in version control.

**DEFAULT_AUTO_FIELD**: If you encounter warnings about this setting, add the following to your `settings.py` (not in `.env`):
```python
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
```
This defines the default primary key field type for models when not explicitly specified.
