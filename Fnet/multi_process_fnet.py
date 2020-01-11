import requests
import datetime
import multiprocessing
import time
import re
import sys
import os


import xlrd


"""多进程下载F-net网站地震数据"""
class Client():
    """Client for f-net server """
    FNET = "http://www.fnet.bosai.go.jp/auth/dataget/"
    DATAGET = FNET + "cgi-bin/dataget.cgi"
    DATADOWN = FNET + "dlDialogue.php"


    """初始化Client类"""
    def __init__(self, user, password, proxies=None, timeout=120):
        self.session = requests.session()
        self.session.auth = (user, password)
        self.proxies = proxies
        self.timeout = timeout
        print("执行了__init__")


    """定义获取下载数据的url链接，创建进程池，和队列"""
    def get_url(
            self,
            data,
            q_url,

    ):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("get_url启动,子进程（%s）,父进程为（%s）" %(os.getpid(), os.getppid()))
        print(data)
        time.sleep(5)

        r = self.session.post(self.DATAGET, auth=self.session.auth, data=data, proxies=self.proxies)
        print(r.status_code)
        print(r.text)
        if r.status_code == 401:  # username is right, password is wrong
            sys.exit("Unauthorized! Please check your username and password!")
        elif r.status_code == 500:  # internal server error, or username is wrong
            sys.exit("Internal server error! Or you're using the wrong username!")
        elif r.status_code != 200:
            sys.exit("Something wrong happened! Status code = %d" % (r.status_code))

       # 提取数据ID
        m = re.search(r"dataget\.cgi\?data=(NIED_\d+\.zip)&", r.text)

        if m:
            data_id = m.group(1)
            print("当前获取到的ID号(%s),等待进一步解析"%(data_id))
        else:
            sys.stderr.write(r.text)
            sys.exit("解析网页错误")

        # check if data preparation is done
        r = self.session.get(self.DATAGET + "?data=" + data_id,
                             auth=self.session.auth, proxies=self.proxies)
        if "Our data server is very busy now." in r.text:
            print("当前(%s)号子进程出现问题" %(os.getppid()))
            print(r.text)
            sys.stderr.write("Something wrong with the F-net server.\n")
            return None
        if "Your request has been rejected because the total file size exceeds 50 MB." in r.text:
            sys.stderr.write("Your request has been rejected because the total file size exceeds 50 MB.")
            return None
        url_down = self.DATADOWN + "?_f=" + data_id
        #  将现在链接放入url队列
        q_url.put(url_down)
        print("当前获取的下载url:", url_down)
        print("当前队列中等待下载url链接数：", q_url.qsize())

    """下载数据，创建进程池，和队列"""
    def download_url(self):
        pass

    """定义获取波形数据的函数"""

    def prepre_data(
            self,
            q,
            starttime,
            end='time',
            endtime=None,
            duration_in_seconds=None,
            format="SAC",
            station="ALL",
            component="LH?",
            time="UT",
            path_save="./",
            filename=None,
    ):
        """Get waveform data from NIED F-net."""

        if starttime.year < 1995:
            raise ValueError("No data avaiable before year 1995.")

        # BH? => BHX
        component = component.replace("?", "X")

        if end == 'time':
            data0 = {
                "end": "time",
                "e_year": endtime.strftime("%Y"),
                "e_month": endtime.strftime("%m"),
                "e_day": endtime.strftime("%d"),
                "e_hour": endtime.strftime("%H"),
                "e_min": endtime.strftime("%M"),
                "e_sec": endtime.strftime("%S"),
            }
        elif end == 'duration':
            data0 = {
                "end": "duration",
                "sec": duration_in_seconds,
            }

        data1 = {
            "s_year": starttime.strftime("%Y"),
            "s_month": starttime.strftime("%m"),
            "s_day": starttime.strftime("%d"),
            "s_hour": starttime.strftime("%H"),
            "s_min": starttime.strftime("%M"),
            "s_sec": starttime.strftime("%S"),
            "format": format,
            "archive": "zip",  # always use ZIP format
            "station": station,
            "component": component,
            "time": time,
        }
        data = data0.copy()
        data.update(data1)
        # 将多个data放入data队列中
        q.put(data)
        print("prepre_data中队列大小：",q.qsize())
        print("运行prepre_data")
        


    # def main():
    #     pass

if __name__=="__main__":
    """
    目前存在的问题：
    1.可以实现多进程，但是多进程会导致网站服务发生错误！
    2.难道是因为同时发出的请求太多？如果将下载同时进行怎么样？

    """
    print("进程（%s）" % os.getpid())
    year_start = 2016
    year_end = 2016
    """创建data队列"""
    q_data = multiprocessing.Manager().Queue()
    client = Client("zjq02010", "zjq347634")
    for month in range(1,2):
        if month < 12:
            month_end = month+1
        elif month == 12:
            year_end = 2017
            month_end = 1

        starttime = datetime.datetime(year_start, month, 1, 0, 0)
        endtime = datetime.datetime(year_end, month_end, 1, 0, 0)
        print(starttime,'\n',endtime)
        # 读取Fnet地震台站台站名称，因人而异
        workbook = xlrd.open_workbook('/mnt/e/data(2019)/fnet台站坐标信息.xlsx')
        sheet = workbook.sheet_by_name('Sheet1')
        print('sheet name:',sheet.name)
        print('sheet column:', sheet.ncols)
        print('sheet row:',sheet.nrows)
        Station_all = sheet.col_values(0,1,)

        for i in range(0,len(Station_all),3):
            d = len(Station_all)-i
            if d < 3:
                station = Station_all[i:i+d]
                print(Station_all[i:i+d], 'over')
            else:
                station = Station_all[i:i+3]
                print(station)
       #         time.sleep(3)

            # 将需要发送给服务器的数据，加入列队，等到get_url函数获取并请求
            client.prepre_data(q_data, starttime=starttime, endtime=endtime, station=station, component="LH?")
    time.sleep(3)
    print("主进程（%s）" % os.getpid())
    q_url = multiprocessing.Manager().Queue()
    po_get_url = multiprocessing.Pool(3)
    count_all = q_data.qsize()
    count1 = count_all
    print(count_all)
    while count1:
        print("子进程正在处理第(%s)个data请求，一共(%s)个" %(count1,count_all))
        data_send = q_data.get() 
        po_get_url.apply_async(client.get_url, args=(data_send, q_url,))
        count1 = q_data.qsize()
        #time.sleep(5)
       # print("运行完子进程")
    po_get_url.close()
    po_get_url.join()
    print("进程（%s）结束" %os.getpid())



