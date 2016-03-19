sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -s /home/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
