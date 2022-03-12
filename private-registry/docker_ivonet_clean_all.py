#!/usr/bin/env python

import subprocess

PRIVATE_REPO = "docker.ivonet.nl"
FILE_OUTPUT = "docker_ivonet_clean_all.sh"


def run_process(exe):
    'Define a function for running commands and capturing stdout line by line'
    p = subprocess.Popen(exe.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')


def main():
    cmd = 'docker images'
    fo = open(FILE_OUTPUT, "w")
    fo.write("#!/bin/sh\n")

    # Run the command and capture the output line by line.
    first = True
    for line in run_process(cmd):
        if first:
            first = False
            continue
        line.strip()
        items = line.split()
        tagname = "%s:%s" % (items[0], items[1],)
        if PRIVATE_REPO in line:
            output = "docker rmi %s" % (tagname,)
            fo.write("%s\n" % output)
            print output
    fo.close()
    run_process("chmod +x %s" % FILE_OUTPUT)


if __name__ == '__main__':
    main()
