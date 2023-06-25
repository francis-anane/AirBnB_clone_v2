#!/usr/bin/python3
"""Script for fabric that distributes an archive to web servers
"""

from datetime import datetime
from fabric.api import env, run, local, put, runs_once
import os

env.hosts = ["54.144.150.155", "3.89.155.218"]
env.user = "ubuntu"


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


def do_deploy(archive_path):
    """Deploy archive
    Args:
        archive_path (str): The path of the archive to deploy.
    Return: True if the path exists and the operation succeeds, or
    False otherwise.
    """
    if os.path.exists(archive_path):
        upload_file = archive_path.split("/")[1]
        extract_src = "/tmp/" + upload_file
        extract_dest = "/data/web_static/releases/"+upload_file.split(".")[0]
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(extract_dest))
        run("sudo tar -xzf {} -C {}".format(extract_src, extract_dest))
        run("sudo rm {}".format(extract_src))
        run("""for f in `sudo ls {0}/web_static`;
        do sudo mv {0}/web_static/$f {0}/$f;
        done""".format(extract_dest))
        run("sudo rm -rf {}/web_static".format(extract_dest))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(extract_dest))

        print("New version deployed!")
        return True

    return False
