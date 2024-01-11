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
        upload = put(archive_path, "/tmp/")
        if upload.failed:
            return False
        res = run(f"mkdir -p /data/web_static/releases/{name_dir}/")
        if res.failed:
            return False
        res = run(f"mkdir -p /data/web_static/current/")
        with cd("/data/web_static/releases/"):
            cmd = f"tar -xzf /tmp/{name_dir}.tgz -C {name_dir}"
            res1 = run(cmd)
            if res1.failed:
                return False
            run(f"rm /tmp/{name_file}.tgz")
            res2 = run(f"ln -sf {name_file} /data/web_static/current")
            if res2.failed:
                return False
        return True
    else:
        return False
