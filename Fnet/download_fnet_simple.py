from FnetPy import Client
from datetime import datetime
from threading import Thread
import time
from multiprocessing import Process

# proxy = {'http': 'http://127.0.0.1:10809',
#          'https':'https://127.0.0.1:10809'}
proxy = None
starttime = datetime(2015, 3, 1, 0, 0)
endtime = datetime(2015, 4, 1, 0, 0)
starttime2 = datetime(2015, 3, 1, 0, 0)
starttime3 = datetime(2015, 4, 1, 0, 0)
endtime2 = datetime(2015, 5, 1, 0, 0)
duration_time = 300
client = Client("zjq02010", "zjq347634", proxies=proxy)
if __name__=="__main__":
    t1 = Thread(target=client.get_waveform, args=(starttime, 'time', endtime,  duration_time, "SAC", "ABU", "LH?"))
    t2 = Thread(target=client.get_waveform, args=(starttime2, 'time', endtime2,  duration_time, "SAC", "ABU", "LH?"))
    t3 = Thread(target=client.get_waveform, args=(starttime3, 'time', endtime2,  duration_time, "SAC", "ABU", "LH?"))
    t4 = Thread(target=client.get_waveform, args=(starttime3, 'time', endtime2,  duration_time, "SAC", "ABU", "LH?"))
    t5 = Thread(target=client.get_waveform, args=(starttime3, 'time', endtime2,  duration_time, "SAC", "ABU", "LH?"))
    t6 = Thread(target=client.get_waveform, args=(starttime3, 'time', endtime2,  duration_time, "SAC", "ABU", "LH?"))
    t1.start()
    # time.sleep(15)
    t2.start()
    # time.sleep(15)
    t3.start()
    # time.sleep(15)
    t4.start()
    # time.sleep(15)
    t5.start()
    # time.sleep(15)
    t6.start()


# t1 = client.get_waveform(starttime=starttime, end='duration', endtime=endtime,  duration_in_seconds=duration_time, station="ABU", component="LHZ",format="SEED")


# t2 = client.get_waveform(starttime=starttime2, end='duration', endtime=endtime2,  duration_in_seconds=duration_time, station="ABU", component="LHZ",format="SEED")

