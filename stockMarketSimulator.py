#stock market workload
# In future update script to run asynchronously

import schedule
import subprocess, signal, os
import time
import datetime

secs2=14400 # 4 hrs interval

# Run only on weekdays
def startScheduler():
    day = datetime.datetime.today().isoweekday()
    if day != 6 or day!=7:
        f2()
        f3()
        f2()
    else:
        time.sleep(86500)

def f2():
    print("simulating stress at 80%")
    pro = subprocess.Popen("stress-ng -c 1 -l 80", stdout=subprocess.PIPE,
                    shell=True, preexec_fn=os.setsid)
    time.sleep(3600) #9-10 && 2.30-3.30
    os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
    time.sleep(5)
    print("terminated stress at 80%")

def f3():
    print("simulating stress at 60%")
    pro = subprocess.Popen("stress-ng -c 1 -l 60", stdout=subprocess.PIPE,
                    shell=True, preexec_fn=os.setsid)
    time.sleep(16200) #10-2:30
    os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
    time.sleep(5)
    print("terminated stress at 60%")

def main():
    print("Running Load Script")
    schedule.every().day.at("09:00").do(startScheduler)

    while True:
        schedule.run_pending()
        time.sleep(1)

main()
