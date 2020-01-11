from FnetPy import Client
from datetime import datetime
import xlrd

# 下载得数据保存路径
savepath = 'C:\\Users\\Administrator\\Desktop\\test\\'
# 如果需要使用代理
proxy = {'http': 'http://127.0.0.1:10809',
         'https':'https://127.0.0.1:10809'}
# 响应头中浏览器信息，Fnet基本不反爬，不设置也行
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
# 下载哪一年数据
year_start = 2016
year_end = 2016
for month in range(1,13):
    if month < 12:
        month_end = month+1
    elif month == 12:
        year_end = 2017
        month_end = 1

    starttime = datetime(year_start,month, 1, 0, 0)
    endtime = datetime(year_end, month_end, 1, 0, 0)
    print(starttime,'\n',endtime)
    # 读取Fnet地震台站台站名称，因人而异
    workbook = xlrd.open_workbook(r'E:\data(2019)\fnet台站坐标信息.xlsx')
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

        client = Client("zjq02010", "zjq347634")
        client.get_waveform(path_save=savepath, starttime=starttime, endtime=endtime, station=station, component="LH?")#, proxies=proxy)

