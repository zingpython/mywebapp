```
STATIC_URL = '/static/'       
STATIC_ROOT = '/var/www/env/mywebapp/ourrecords/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '/var/www/env/mywebapp/ourrecords/staticfiles/')
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '/var/www/env/mywebapp/ourrecords/media/')
```