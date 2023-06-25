#!/usr/bin/python3
"""A script for fabric that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """To archive the web_static files."""
    if not os.path.isdir("versions"):
        local("mkdir versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    out_file = "versions/web_static_{}.tgz".format(date)
    try:
        print("Packing web_static to {}".format(out_file))
        local("tar -cvzf {} web_static".format(out_file))
        size = os.stat(out_file).st_size
        print("web_static packed: {} -> {} Bytes".format(out_file, size))
    except Exception:
        out_file = None
    return out_file
