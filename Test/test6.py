import datetime
import os
# 关于时间模块datetime的测试

# 设定特定时间
# timestop = datetime.datetime(2019, 9, 3, 17, 3, 0)
# while datetime.datetime.now() < timestop:
#     print("Program is sleeping.", end="")
# print("Wake up !")

# 日期与一段时间相加
deltaTime = datetime.timedelta(days=100)
timenow = datetime.datetime.now()
print("现在的时间是：",timenow)
print("100天后是：",timenow + deltaTime)
os.system("python msg_free.py")

