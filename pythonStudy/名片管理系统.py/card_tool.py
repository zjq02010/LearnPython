# 名片操作系统函数组件

cardList = []

# 主菜单
"""
这是试试
"""


def showMenu():
    """
    这是注释
    """
    print("")
    print("***************** 欢迎来到名片管理系统 V1.0 *****************")
    print("1. 查询名片")
    print("2. 新增名片")
    print("3. 删除名片")
    print("")
    print("0. 退出系统")
    print("-"*60)


# 名片查询/修改函数
def cardLookEdit():
    print("姓名\t\t年龄\t\t邮箱")
    if len(cardList) == 0:
        print("当前系统无名片，请新建")
        return
    else:
        for card in cardList:
            print(card["name"], "\t\t", card["age"], "\t\t", card["mail"])
        else:
            print("-"*60)

            while True:
                option = input("请输入需要进行的操作【1.编辑】【2.返回】：")
                if option == "1":
                    nameEdit = input("请输入需要修改的人员姓名：")
                    for cardFind in cardList:
                        if cardFind["name"] == nameEdit:
                            print("原始信息\n姓名：%s\t\t年龄:%d\t\t邮箱：%s" % (cardFind["name"], cardFind["age"], cardFind["mail"]))
                            nameNew = input("请输入新名字【回车不修改】")
                            ageNew = input("请输入新年龄【回车不修改】")
                            mailNew = input("请输入新邮箱【回车不修改】")
                            if nameNew != "":
                                cardFind["name"] = nameNew
                            if ageNew != "":
                                cardFind["age"] = int(ageNew)
                            if mailNew != "":
                                cardFind["mail"] = mailNew
                            print("-"*60)
                            print("修改成功")
                            print("修改后信息\n姓名：%s\t\t年龄:%d\t\t邮箱：%s" % (cardFind["name"], cardFind["age"], cardFind["mail"]))
                            return
                    else:
                        print("输入错误，查无此人")
                elif option == "2":
                    break
                else:
                    print("输入错误，请重新输入")


# 名片新增函数
def cardAdd():
    name = input("请输入新增人员姓名：")
    age = int(input("请输入新增人员年龄："))
    mail = input("请输入新增人员邮箱：")
    cardTmp = {
        "name": name,
        "age": age,
        "mail": mail,
    }
    cardList.append(cardTmp)
    print("-"*60)
    print("新增名片成功")
    print("新增名片信息:")
    print("姓名：%s\t\t年龄:%d\t\t邮箱：%s" % (cardTmp["name"], cardTmp["age"], cardTmp["mail"]))


# 名片删除函数
def card_Del():
    name = input("请输入需要删除的人员姓名：")
    for dic in cardList:
        if dic["name"] == name:
            cardList.remove(dic)
            print("删除%s成功" % name)
            break
    else:
        print("列表中没有该人员信息，请查正")
