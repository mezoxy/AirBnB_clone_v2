#!/usr/bin/python3
'''The module: 1-pack_web_static'''


from fabric.api import local
from datetime import datetime as t


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
