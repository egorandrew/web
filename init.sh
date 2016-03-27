#sudo rm -rf /etc/nginx/sites-enabled/default
#sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
#sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
mysql -uroot -e "create database ask_web;"
mysql -uroot -e "CREATE USER 'enth'@'localhost' IDENTIFIED BY '';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON *.* TO 'enth'@'localhost';"
