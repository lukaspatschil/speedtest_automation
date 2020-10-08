#!/usr/bin/env python3

from os.path import isfile, join
from os import listdir
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

path = './out'

filenames = [f for f in listdir(path) if isfile(join(path, f))]
dates = []
speeds = []

for file in filenames:
    dates.append(file.split('.')[0].replace('-', '.'))

    f = open(join(path, file))

    dataSum = 0
    lineCount = 0
    for line in f:
        dataSum += float(line.split(';')[1])
        lineCount += 1

    speeds.append(round(dataSum / lineCount, 2))

print(speeds)

y_pos = np.arange(len(dates))
print(y_pos)
plt.bar(y_pos, speeds, align='center', alpha=0.5)
plt.xticks(y_pos, dates)
plt.ylabel('Speed in Mbit/s')
plt.title('Internet speed')

average = sum(speeds) / len(speeds)

print(average)

plt.hlines(average, 0, len(dates), colors='red')

plt.show()
