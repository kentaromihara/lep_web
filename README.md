# lep_web


## commit rule
### commit message category
- [ADD] : New feature/file added
- [UPD] : Code has been modified
- [DEL] : File deleted
- [RES] : Conflict resolved


## userful notes

- to find a password for wordpress   
https://docs.bitnami.com/aws/faq/get-started/find-credentials/

 - to allow the https for flask+wsgi  
https://own-search-and-study.xyz/2018/07/21/%E7%84%A1%E6%96%99%E3%81%A7https%E5%AF%BE%E5%BF%9C%E3%81%97%E3%81%9F%E8%87%AA%E4%BD%9Cweb%E3%82%B5%E3%82%A4%E3%83%88%E3%82%92%E5%85%AC%E9%96%8B%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/

- for /etc/apache2/sites-available/flask.conf  
        WSGIScriptAlias / /var/www/flask/wsgi.py  
        WSGIDaemonProcess flask python-path=/var/www/flask:/var/www/flask/env/lib/python3.5/site-packages  
        WSGIProcessGroup flask  

- to implement the google-cloud-translate  
https://pypi.org/project/google-cloud-translate/

- to set the environmental valueables  
/etc/apache2/envvars

- to see the errorlog for apache2  
/var/log/apache2/error_log

- to set the environmental valuable for wsgi, need to write in **wsgi.py**, for example,
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/var/www/flask/.gcp/my_service_account_file_name'

- when got error **locale.Error: unsupported locale setting**  
export LC_ALL="en_US.UTF-8"  
export LC_CTYPE="en_US.UTF-8"   
sudo dpkg-reconfigure locales  

- when you want to pip install for flask on wsgi and apache, need to set full path  
sudo /var/www/flask/env/bin/pip3.5 install <some library>
