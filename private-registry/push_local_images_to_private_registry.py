#!/usr/bin/env python

import subprocess

PRIVATE_REPO = "192.168.1.100:8083"

def runProcess(exe):
    'Define a function for running commands and capturing stdout line by line'
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')


# Get all filenames in working directory


def main():
    cmd = 'docker images'
    fo = open("push.sh", "w")
    fo.write("#!/bin/sh\n")

    # Run the command and capture the output line by line.
    first = True
    skip = []
    for line in runProcess(cmd.split()):
        if first:
            first = False
            continue
        line.strip()
        items = line.split()
        tagname = "%s:%s" % (items[0], items[1],)
        tagname = tagname.replace("%s/" % PRIVATE_REPO, "")
        if "192.168.1.100" in line:
            skip.append(tagname.replace("%s/" % PRIVATE_REPO, ""))
            print "skip", tagname
            continue
        if tagname in skip:
            print "skipping", tagname
            continue
        output = "docker tag %s %s/%s" % (items[2], PRIVATE_REPO, tagname,)
        fo.write("%s\n" % output)
        print output
        output = "docker push %s/%s" % (PRIVATE_REPO, tagname,)
        fo.write("%s\n" % output)
        print output
        # output = "docker rmi %s/%s" % (PRIVATE_REPO, tagname,)
        # fo.write("%s\n" % output)
        # print output
    fo.close()


if __name__ == '__main__':
    main()
