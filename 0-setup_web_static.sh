#!/usr/bin/env bash
# Set up your web servers for the deployment of web_static
sudo apt update -y
sudo apt install -y nginx
sudo service nginx start
mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sudo chown -R ubuntu:ubuntu /data/
echo "Hi Dear, I'm Ayoub" > /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo sed -i "s#server_name _;#server_name _;\n\n\tlocation /hbnb_static {\n\t\talias  /data/web_static/current/;\n\t}#" /etc/nginx/sites-enabled/default
sudo service nginx reload
