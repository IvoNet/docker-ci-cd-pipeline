#!/usr/bin/env python

import subprocess


def runProcess(exe):
    """Define a function for running commands and capturing stdout line by line"""
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')


def main():
    cmd = 'docker images'
    fo = open("remove.sh", "w")
    fo.write("#!/bin/sh\n")

    # Run the command and capture the output line by line.
    first = True
    for line in runProcess(cmd.split()):
        if first:
            first = False
            continue
        line.strip()
        items = line.split()
        imageId = "%s" % (items[2],)
        if "<none>" in line:
            output = "docker rmi %s" % (imageId,)
            fo.write("%s\n" % output)
            print output
    fo.close()
    runProcess("chmod +x remove.sh".split())

if __name__ == '__main__':
    main()
