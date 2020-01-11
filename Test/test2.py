import multiprocessing
import os
import time
import random

def read(q1):
    print("test启动（%s）,父进程为（%s）" %(os.getpid(), os.getppid()))
    print(q1.get())
    for i in range(q1.qsize()):
        print("read从Queue中获取到消息：%s" % q1.get())
    # b1 = q2.get(True)

def write(q):
    # print("write启动（%s）,父进程为（%s）" % (os.getpid(), os.getppid()))
    for i in "python":
        print(i)
        q.put(i)

    time.sleep(random.random())

def main():
    print("进程（%s）" % os.getpid())
    q = multiprocessing.Manager().Queue()
    print(q.qsize())
    po = multiprocessing.Pool(3)
    po.apply_async(write, args=(q,))
    time.sleep(3)
    print(q.qsize())
    po.apply_async(read, args=(q,))
    po.close()
    po.join()
    print("结束")

if __name__ == '__main__':
    main()