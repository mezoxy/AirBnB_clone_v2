#!/usr/bin/python3
'''The module: 1-pack_web_static'''


from fabric.api import local, put, run, env
import re
from os.path import exists
from datetime import datetime as t


env.hosts = ['54.237.35.210', '34.239.107.142']


def do_pack():
    """
        Function: do_pack
        use: generates a .tgz archive from the contents of the web_static
    """
    time = t.now().strftime("%Y%m%d%H%M%S")
    creat = "mkdir -p ./versions/ && "
    tar_cmd = "tar -cvzf versions/web_static_{}.tgz web_static".format(time)
    cmd = creat + tar_cmd
    val = local(cmd)
    if val.succeeded:
        return "versions/web_static_{}.tgz".format(time)
    return None


def do_deploy(archive_path):
    """
        Function: do_deploy
        Returns False if the file at the path archive_path
    """
    if exists(archive_path):
        name_dir = re.match(r'.*(web_static_\d*)', archive_path).group(1)
        try:
            put(archive_path, "/tmp/")
            run(f"sudo mkdir -p /data/web_static/releases/{name_dir}/")
            location = f"/data/web_static/releases/{name_dir}"
            run(f"sudo tar -xzf /tmp/{name_dir}.tgz -C {location}")
            run(f"sudo rm /tmp/{name_dir}.tgz")
            run(f"sudo mv {location}/web_static/* {location}/")
            run(f"sudo rm -rf {location}/web_static")
            run(f"sudo rm -rf /data/web_static/current")
            run(f"sudo ln -s {location}/ /data/web_static/current")
        except Exception:
            return False
    else:
        return False

def deploy():
    """
        Function: deploy
        Returns: The value of 
