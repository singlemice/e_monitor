# -*- coding: utf-8 -*-
__author__ = 'TaurenDruid'

import urllib
import datetime,os
from time import sleep


def writeToLog(logmsg):
    try:
        logfile=os.path.join(os.getcwd(),'check_status.txt')

        f = open(logfile, 'a')
    except Exception as e:
        print "unable to open log file"
    try:
        f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " | " + logmsg + "\n")
        f.close()
    except Exception as e:
        print "unable to open log file2 "
i_200=0
i_500=0
while 1:
    res=urllib.urlopen('http://www.baidu.com')
    code=str(res.getcode())
    writeToLog(str(res.getcode()))


    if code=='200':
        i_200 = i_200 + 1

        sleep(1)

    else:
        i_500=i_500+1

        pass

    print ("status:200  count:%s   --   status:503 count:%s" %(i_200, i_500))

