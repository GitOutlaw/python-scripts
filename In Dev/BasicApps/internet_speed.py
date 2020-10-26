import speedtest
import datetime
import time

s = speedtest.Speedtest()


time_now = datetime.datetime.now().strftime("%H:%M:%S")
downspeed = round((round(s.download()) / 1048576), 2)
upspeed = round((round(s.upload()) / 1048576), 2)
print(f"Time: {time_now}, Downspeed: {downspeed} Mb/s, Upspeed: {upspeed} Mb/s")
