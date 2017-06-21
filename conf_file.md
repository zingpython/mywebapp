```
<VirtualHost *:80>
ServerName localhost
ServerAdmin webmaster@localhost

Alias /static /var/www/env/mywebapp/ourrecords/static
<Directory /var/www/env/mywebapp/ourrecords/static>
   Require all granted
 </Directory>

Alias /media /var/www/env/mywebapp/ourrecords/media
<Directory /var/www/env/mywebapp/ourrecords/media>
   Require all granted
</Directory>

<Directory /var/www/env/mywebapp/ourrecords/ourrecords>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>

WSGIDaemonProcess home python-path=/var/www/env/mywebapp/ourrecords/:/var/www/env/lib/python3.5/site-packages
WSGIProcessGroup home
WSGIScriptAlias / /var/www/env/mywebapp/ourrecords/ourrecords/wsgi.py


ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```