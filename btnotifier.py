import psutil
from plyer import notification
import time

while (True):
    battery = psutil.sensors_battery()
    percent = battery.percent

    notification.notify(
      title = "Battery Remining",
      message = str(percent)+"%Battery remining",
      timeout = 10
    )
# send notification for every 60 mins
    time.sleep(60*60)

    continue
