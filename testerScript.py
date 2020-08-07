from datetime import datetime
import speedtest

unit = 1000000

for i in range(10):
    now = datetime.now()
    testDate = now.strftime("%d/%m/%Y %H:%M:%S")
    filename = "out/" + now.strftime("%Y-%m-%d") + ".a"
    st = speedtest.Speedtest()

    downloadTest = round(st.download() / unit, 2)

    f = open(filename, "a")
    f.write(testDate + ';' + str(downloadTest) + '\n')
    f.close()
    print('DONE')

#print('Speed: ' + str(downloadTest) + '; Time: ' + testDate)
