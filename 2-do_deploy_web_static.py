#!/usr/bin/python3
'''The module: 1-pack_web_static'''


from fabric.api import put, run, sudo, env, cd

env.hosts = ['54.237.35.210', '34.239.107.142']


def do_deploy(archive_path):
    import re
    """
        Function: do_deploy
        Returns False if the file at the path archive_path doesn’t exist
    """
    if archive_path:
        name_file = re.match(r'.*(web_static_\d*)', archive_path).group(1)
        upload = put(archive_path, '/tmp')
        if upload.failed:
            return False
        res = run("mkdir -p /data/web_static/releases/")
        if res.failed:
            return False
        with cd("/data/web_static/releases/"):
            res1 = run(f"mkdir -p {name_file} && tar -xvf /tmp/{name_file}.tgz -C {name_file}")
            if res1.failed:
                return False
            run(f"rm /tmp/{name_file}.tgz")
            res2 = run(f"ln -sf {name_file} /data/web_static/current")
            if res2.failed:
                return False
        return True
    else:
        return False

