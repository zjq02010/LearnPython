# 字典的常用操作
# 列表是有序的对象集合
# 字典是无序的对象集合，使用{}表示，键值对形式储存
# 字典的键唯一，值可以使用任何形式的数据类型
mm = {
    "name": "mm",
    "age": 18,
    "gender": "woman",
}
print(mm)
# 取值
print(mm["age"])
# 增加/修改
mm["hobby"] = "dance"  # 如果以前没有，则新增
print(mm)
mm["age"] = 16  # 如果以前有，则修改
print(mm)
# 删除
mm.pop("hobby")
print(mm)

# 统计键值对数量
print(len(mm))
# 合并字典
dic2 = {"city": "Wuhan"}
mm.update(dic2)
print(mm)
# 清空字典
dic2.clear()
print(dic2)

# for循环遍历字典
# 循环时，循环变量为字典的key
for k in mm:
    print(k)
    print("字典的键：%s,字典的值：%s" % (k, mm[k]))
