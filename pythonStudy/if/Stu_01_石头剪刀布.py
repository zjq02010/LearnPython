# 需求：模拟石头剪刀布的过程
# 2020.1.9
import random

# 1. 玩家输入石头（1）剪刀（2）布（3）；
player = int(input("请玩家输入石头（1）剪刀（2）布（3）："))
# 2. 电脑随机生成石头（1）剪刀（2）布（3）；
computer = random.randint(1, 3)
print("玩家输入的是：%d, 电脑输入的是：%d\n" % (player, computer))
# 3. 判断比较
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or(player == 3 and computer == 1)):
    print("恭喜玩家获胜")
elif player == computer:
    print("平局啦")
else:
    print("玩家输啦")
