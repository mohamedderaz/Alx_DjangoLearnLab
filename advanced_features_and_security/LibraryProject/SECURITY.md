# HTTPS & Security Configuration Summary

## Enforced Settings in settings.py:
- SECURE_SSL_REDIRECT = True
- SECURE_HSTS_SECONDS = 31536000
- SECURE_HSTS_INCLUDE_SUBDOMAINS = True
- SECURE_HSTS_PRELOAD = True
- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SECURE = True
- X_FRAME_OPTIONS = 'DENY'
- SECURE_CONTENT_TYPE_NOSNIFF = True
- SECURE_BROWSER_XSS_FILTER = True

## Deployment Notes:
- SSL certificates installed via Let's Encrypt
- Nginx configured to redirect all HTTP to HTTPS
- HTTP headers enforced using Django and Nginx