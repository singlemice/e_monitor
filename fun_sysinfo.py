# -*- coding: utf-8 -*-
__author__ = 'TaurenDruid'
import subprocess

def uname_func():
    uname = "uname"
    uname_args = "-a"
    print "Gathering System information with %s command:\n" % uname
    subprocess.call([uname,uname_args])


def disk_func():

    diskspace = "df"
    diskspace_args = "-h"
    print "Gathering system information %s command:\n" % diskspace
    subprocess.call([diskspace,diskspace_args])

def main():
    uname_func()
    disk_func()

if __name__=="__main__":
    main()