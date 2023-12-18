import schedule
import subprocess, signal, os
import time
from datetime import datetime, timedelta
from threading import Timer

stress=70
count=10/float(30)
def f():
    global count, stress
    stress += count
    starter2 = Timer(2, f2)
    starter2.start()

def f2():
    print("simulating stress at" + str(stress))
    pro = subprocess.Popen("stress-ng -c 1 -l " + str(stress), stdout=subprocess.PIPE,
                    shell=True, preexec_fn=os.setsid)
    time.sleep(86300)
    # p2.send_signal(signal.CTRL_C_EVENT)
    os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
    time.sleep(2)
    print("terminated stress at"+ str(stress))

def main():
    print("Running Load Script")
    schedule.every().day.at("10:40").do(f)

    while True:
        schedule.run_pending()
        time.sleep(1)

main()
