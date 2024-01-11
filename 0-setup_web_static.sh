#!/usr/bin/env bash
# Set up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install -y nginx
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sudo chown -Rh ubuntu:ubuntu /data/
echo "<h1>Hi Dear, I'm Ayoub</h1>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo sed -i "s#server_name _;#server_name _;\n\n\tlocation /hbnb_static {\n\t\talias  /data/web_static/current/;\n\t}#" /etc/nginx/sites-enabled/default
sudo service nginx restart