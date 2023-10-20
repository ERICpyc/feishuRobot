from datetime import date, datetime

import time
import os
from apscheduler.schedulers.background import BackgroundScheduler

#  放置要运行的脚本
def tick():
    print("tick ! the time is : %s" % datetime.now())
    os.system("../function/vehicle_progress.py")

#  设置起始时间和间隔时间，执行时间间隔可以按照days,minutes,seconds设置
if __name__ == "__main__":
    scheduler = BackgroundScheduler()

    scheduler.add_job(tick, 'interval', days=1, start_date="2022-10-8 14:51:25")

    scheduler.start()

    print("Press Ctrl + {0} to exit".format('Break' if os.name == 'nt' else 'C'))
    try:

        while True:
            time.sleep(30)
            print(f"sleep! - {datetime.now()}")

    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Exit The Job !")