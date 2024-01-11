#!/usr/bin/python3
'''The module: 1-pack_web_static'''


from fabric.api import put, run, sudo, env, cd
import re
from os.path import exists


env.hosts = ['54.237.35.210', '34.239.107.142']


def do_deploy(archive_path):
    """
        Function: do_deploy
        Returns False if the file at the path archive_path
    """
    if exists(archive_path):
        name_dir = re.match(r'.*(web_static_\d*)', archive_path).group(1)
        if put(archive_path, "/tmp/").failed:
            return False
        if run(f"mkdir -p /data/web_static/releases/{name_dir}/").failed:
            return False
        location = f"/data/web_static/releases/{name_dir}"
        if run(f"tar -xzf /tmp/{name_dir}.tgz -C {location}").failed:
            return False
        if run(f"rm /tmp/{name_dir}.tgz").failed:
            return False
        if run(f"ln -sf {location} /data/web_static/current").failed:
            return False
        return True
    else:
        return False
