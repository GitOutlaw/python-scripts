import matplotlib.pyplot as plt
import csv
import matplotlib.ticker as ticker

times = []
download = []
upload = []


with open('D:/dev/gits/Python-Scripts/internet_speed_test/data/internet_test.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in plots:
        times.append(str(row[0]))
        download.append(float(row[1]))
        upload.append(float(row[2]))

print(times, "\n", download, "\n", upload)
