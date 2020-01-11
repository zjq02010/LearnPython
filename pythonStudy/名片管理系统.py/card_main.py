import card_tool
# 名片管理系统
# 实现名片的增删改查功能1

# TODO(zjq) 显示菜单
# 主程序入口
while True:
    card_tool.showMenu()
    option = input("请输入选择的操作需要：")
    print("-"*60)
    if option == "1":
        # 名片查询函数
        card_tool.cardLookEdit()
    elif option == "2":
        # 新增名片函数1
        card_tool.cardAdd()
    elif option == "3":
        # 删除名片函数
        card_tool.card_Del()
    elif option == "0":
        # 退出系统
        break
    else:
        print("输入错误，请重新输入!!!")
