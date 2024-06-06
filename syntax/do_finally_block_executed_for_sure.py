import signal
import sys
import time


signal.signal(signal.SIGINT, lambda sig, frame: sys.exit(1))

try:
    while True:
        print("On")
        time.sleep(1)
finally:
    print('Off boy')
