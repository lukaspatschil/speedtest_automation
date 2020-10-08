#!/usr/bin/env python3

from datetime import datetime
import speedtest
import os

unit = 1000000

st = speedtest.Speedtest()

path = "/home/pi/python/out"


now = datetime.now()
testDate = now.strftime("%d/%m/%Y %H:%M:%S")
filename = now.strftime("%Y-%m-%d") + ".a"

downloadTest = round(st.download() / unit, 2)

f = open(os.path.join(path, filename), "a")
f.write(testDate + ';' + str(downloadTest) + '\n')
f.close()
print('DONE')
