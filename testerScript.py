#!/usr/bin/env python

from datetime import datetime
import speedtest
import os

unit = 1000000

st = speedtest.Speedtest()

path = "/home/pi/python/"


now = datetime.now()
testDate = now.strftime("%d/%m/%Y %H:%M:%S")
filename = "out/" + now.strftime("%Y-%m-%d") + ".a"

downloadTest = round(st.download() / unit, 2)

f = open(os.path.join(path, filename), "a")
f.write(testDate + ';' + str(downloadTest) + '\n')
f.close()
print('DONE')
