from selenium import webdriver
import time
import datetime

def login():
    # 打开淘宝登录页，扫码登陆
    browser.get("https://www.taobao.com")
    time.sleep(1)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(0.5)
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

def buy(times):
    while True:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print(now)
        if now > times:
            while True:
                try:
                    if browser.find_element_by_id("J_SelectAll2"):
                        browser.find_element_by_id("J_SelectAll2").click()
                        print("已点击全选")
                        break
                except:
                    print("找不到全选按钮")
            print("代码过了点击全选部分")
            time.sleep(0.3)

            while True:
                try:
                    if browser.find_element_by_link_text("结 算"):
                        browser.find_element_by_link_text("结 算").click()
                        print("结算成功")
                        break
                except:
                    pass
            # 提交订单
            while True:
                try:
                    if browser.find_element_by_link_text("提交订单"):
                        browser.find_element_by_link_text("提交订单").click()
                        now1 = datetime.datetime.now()
                        print("抢购成功时间：%s" % now1)
                except:
                    print("再次提交订单")


            # while True:
            #     try:
            #         i


if __name__ == "__main__":
    chrome_option = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_option.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome()
    browser.maximize_window()
    login()
    times = input("请输入抢购时间，格式如(2018-09-06 11:20:00.000000):")
    buy(times)
