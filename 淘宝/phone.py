from appium import webdriver
import time
import datetime


def swipeUp(driver, t=500, n=1):
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5 # x坐标
    y1 = l['height'] * 0.75 # 起始y坐标
    y2 = l['height'] * 0.25 # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)



if __name__ == "__main__":
    des = {
        'resetKeyboard': True,
        'platformVersion': '7',
        'noReset': True,  # 不将app初始化
        'appActivity': 'com.taobao.tao.TBMainActivity',
        # 'appActivity': '.BrowserActivity',
        'appPackage': 'com.taobao.taobao',
        # 'appPackage': 'com.android.browser',
        'unicodeKeyboard': True,
        'deviceName': '28D6R16907003036',
        'platformName': 'Android'}
    # print(des)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)
    time.sleep(5)
    print("点击ping")
    # 点击购物车
    driver.tap([(1121, 2478)] ,100)
    time.sleep(2)
    # 选择宝贝
    time1 = datetime.datetime.now()
    driver.tap([(95, 539)], 110)
    print("已选择宝贝")
    time.sleep(0.5)
    # 点击结算
    driver.tap([(1433, 2359)], 80)
    print("已点击结算")
    time.sleep(0.45)
    # 提交订单
    driver.tap([(1404, 2480)], 90)
    print("已提交订单")
    time2 = datetime.datetime.now()
    time = time2 - time1
    print(time)
