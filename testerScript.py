from datetime import datetime
import speedtest
import os

unit = 1000000

st = speedtest.Speedtest()

# ! add the path to your out file
path = "/home/pi/python/"

for i in range(10):
    now = datetime.now()
    testDate = now.strftime("%d/%m/%Y %H:%M:%S")
    filename = "out/" + now.strftime("%Y-%m-%d") + ".a"

    downloadTest = round(st.download() / unit, 2)

    f = open(os.path.join(path, filename), "a")
    f.write(testDate + ';' + str(downloadTest) + '\n')
    f.close()
    print('DONE')

#print('Speed: ' + str(downloadTest) + '; Time: ' + testDate)
