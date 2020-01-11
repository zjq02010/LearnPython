# 使用完整的for循环遍历字典的列表
# for else 循环
# 应用场景：迭代遍历嵌套的数据类型，例如一个列表中包含了多个字典
#           判断某一个字典中是否存在某个值
students = [
    {
        "name": "zjq",
        "age": 18,
        "QQ": 123456,
    },
    {
        "name": "mm",
        "age": 10,
        "QQ": 456789
    }
]
findName = "mmm"
for card in students:
    if findName == card["name"]:
        print("找到%s了" % (findName))
        break
    print(card)
# 如果上边查找失败，则会执行下面的内容
else:
    print("没有找到%s了" % (findName))
