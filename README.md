# sw-bac
My first python.
A simple tool to backup cisco router/switch 
you need to replace you switch IP address,username,password in followed contents 
-------------------------------
Host = ‘device ip address’
username = ‘username’
password = ‘password’
-------------------------------
you can also use crontab to backup config everyday
crontab -e
01 1 * * 6 /usr/bin/python /usr/home/zhuxing/backup.py
