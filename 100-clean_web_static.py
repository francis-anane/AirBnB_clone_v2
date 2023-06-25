#!/usr/bin/python3
# A script for fabric, to delete outdated archives.
import os
from fabric.api import *

env.hosts = ["54.144.150.155", "3.89.155.218"]


def do_clean(number=0):
    """Delete outdated archives.
    Args:
        number (int): The number of archives to keep. Keep only the most recent
        archive, if number is 0 or 1, keep the most and second-most recent
        archives if number is 2, etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
