#!/usr/bin/env bash
# Set up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install -y nginx
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo 'Hi Dear, Welcom To our Site' > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i "s#server_name _;#server_name _;\n\n\tlocation /hbnb_static {\n\t\talias  /data/web_static/current/;\n\t}#" /etc/nginx/sites-enabled/default
service nginx restart
