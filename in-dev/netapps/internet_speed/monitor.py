import speedtest
import datetime
import csv
import time
import os

# Instantiate speed test
speed = speedtest.Speedtest()

print('<--- Internet Speed Test --->')
print('<--- Processing --->')
print('<--- Press ctrl + c to exit -->')

# Opens internet_test.csv and writes results - change path to change location mode='w'
with open('E:/dev/gits/python-scripts/python-scripts/in-dev/netapps/internet_speed/data/internet_test.csv', mode='w') as speedcsv:
    # Sets csv writer field names
    csv_writer = csv.DictWriter(
        speedcsv, fieldnames=['time', 'download', 'upload'])
    csv_writer.writeheader()

    while True:
        time_now = datetime.datetime.now().strftime('%m-%d-%Y %I:%M:%S %p')
        downspeed = round((round(speed.download()) / 1048576), 2)
        upspeed = round((round(speed.upload()) / 1048576), 2)
        csv_writer.writerow({
            'time': time_now,
            'download': downspeed,
            'upload': upspeed
        })

        print(
            f"Date and Time: {time_now} | Download: {downspeed} Mb/s | Upload: {upspeed} Mb/s")
        print('<-- Processing -->')
        print('<--- Press ctrl + c to exit -->')
        # 30 seconds sleep
        time.sleep(30)
