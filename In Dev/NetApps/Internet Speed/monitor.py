import speedtest
import datetime
import csv
import time
import os

s = speedtest.Speedtest()

print('<--- Internet Speed Test --->')
print('<-- Processing -->')
print('<--- Press ctrl + c to exit -->')

with open('In Dev/NetApps/Internet Speed/data/internet_test.csv', mode='w') as speedcsv:
    csv_writer = csv.DictWriter(
        speedcsv, fieldnames=['time', 'download', 'upload'])
    csv_writer.writeheader()

    while True:

        time_now = datetime.datetime.now().strftime('%m-%d-%Y %I:%M:%S %p')
        downspeed = round((round(s.download()) / 1048576), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)
        csv_writer.writerow({
            'time': time_now,
            'download': downspeed,
            'upload': upspeed
        })

        print(
            f"Date and Time: {time_now} | Download: {downspeed} Mb/s | Upload: {upspeed} Mb/s")
        print('<-- Processing -->')
        print('<--- Press ctrl + c to exit -->')
        # 60 seconds sleep
        time.sleep(30)
