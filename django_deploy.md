Deploy Django App to Debian Linux Systems
Before Deployment
Change settings.py
Step 1. Make sure you switched Debug to False
Step 2. Change ALLOWED_HOSTS to your IP address
Step 3. Static files
```
STATIC_URL = '/static/'       
STATIC_ROOT = '/var/www/env/your_folder_from_github/your_project/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '/var/www/env/your_folder_from_github/your_project/staticfiles/')
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '/var/www/env/your_folder_from_github/your_project/media/')
```

Get connected
Open terminal and connect to IP address
```
ssh root@ip.address
```
Enter password from your hosting co
Install Apache2 and Python tools
```
sudo apt-get update

sudo apt-get upgrade
 
sudo apt-get install git

sudo apt-get install apache2

sudo apt-get install python-pip python-virtualenv
 
sudo apt-get install python-setuptools python-dev build-essential

sudo apt-get install libapache2-mod-wsgi-py3</code><br/>

sudo apt-get build-dep python-imaging
```
Start Virtualenv and install Python3
```
sudo pip install virtualenv

cd /var/www</code><br/>

mkdir env && cd env

virtualenv -p python3 .

source bin/activate 
```
Check Python version
```
python --version
```
Clone github repo to your server
```
git clone https://github.com/you_github_name/repo_name.git
```
Get into your cloned directory
```
cd your_folder_from_github
```
Install all libriaries from requirements.txt
```
pip install -r requirements.txt
```
Get into your project directory
```
cd your_project
```
Create db and create a super user
```
python manage.py migrate

python manage.py createsuperuser 
```
Create Static & Media Root directories.
Make sure you are in /var/www/venv/your_folder_from_github/your_project/
```
mkdir static

mkdir staticfiles

mkdir media
```

Open 000-default.conf with nano is a text editor

```
sudo nano /etc/apache2/sites-available/000-default.conf
```

Change Apache2 configuration
```
&lt;VirtualHost *:80&gt;
ServerName localhost
ServerAdmin webmaster@localhost

Alias /static /var/www/env/your_folder_from_github/your_project/static
&lt;Directory /var/www/env/your_folder_from_github/your_project/static&gt;
   Require all granted
 &lt;/Directory&gt;

Alias /media /var/www/env/your_folder_from_github/your_project/media
&lt;Directory /var/www/env/your_folder_from_github/your_project/media&gt;
   Require all granted
&lt;/Directory&gt;

&lt;Directory /var/www/env/your_folder_from_github/your_project/your_project&gt;
    &lt;Files wsgi.py&gt;
        Require all granted
    &lt;/Files&gt;
&lt;/Directory&gt;

WSGIDaemonProcess home python-path=/var/www/env/your_folder_from_github/your_project/:/var/www/env/lib/python3.5/site-packages
WSGIProcessGroup home
WSGIScriptAlias / /var/www/env/your_folder_from_github/your_project/your_project/wsgi.py


ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined
&lt;/VirtualHost&gt;
```


Add User Permissions
Add User Permissions (to modify sqlite3 Database). sudo chown is a command to change the ownership of a file/folder at a time to a specified user. CHOWN stands for CHange file OWNer. sudo chmod 755 filename command - you allow everyone to read and execute the file, and the file owner is allowed to write to the file as well. sudo chmod 777 means making the file readable, writable and executable by everyone.

```
sudo adduser $USER www-data
```

```
sudo chown www-data:www-data /var/www/env/your_folder_from_github/your_project/
```

```
sudo chown www-data:www-data /var/www/env/your_folder_from_github/your_project/db.sqlite3
```

```
sudo chmod -R 775 /var/www/env/your_folder_from_github/your_project
```

```
sudo chmod 777 /var/www/env/your_folder_from_github/your_project/media/your_folder_for_images/
```
Collect static files
```
python manage.py collectstatic
```
Restart Apache server
Restart Apache server, do it everytime after changes been made to the site
```
service apache2 restart
```
