import logger_module as log

# print(log.warning("Port 1/2 is UP"))
import time, psutil


def monitor_resources(interval=1):
    print()
    while True:
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        if cpu > 60 or ram > 80:
            print(log.warning(f"HIGH LOAD! CPU:{cpu}%, RAM:{ram}%   "), end="")
        else:
            print(log.info(f"NORMAL LOAD. CPU:{cpu}%, RAM:{ram}%   "), end="")
        print("\r", end="")
        time.sleep(interval)


if __name__ == "__main__":
    try:
        monitor_resources()
    except KeyboardInterrupt as e:
        print()
        print("Bye...")
