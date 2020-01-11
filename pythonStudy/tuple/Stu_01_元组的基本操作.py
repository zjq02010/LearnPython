# 元组（）的基本操作
# 与数组相似，但是元组不能修改
# 定义只有一个元素的元组
# info_tuple = ("zjq" )
info_tuple = ("zjq", 18, "yingkou")
print(info_tuple)
print(type(info_tuple))
# 元组Tuple index
info_index = info_tuple.index(18)
print(info_index)

# 元组Tuple count
info_count = info_tuple.count("zjq")
print(info_index)

#  元组的循环遍历 for循环
# 应用场景
#   1. 函数的输入输出
#   2. 格式化字符串:格式化字符串后面的（）本质上是元组
print("%s今年%d岁，来自%s\n" % info_tuple)
#   3. 让列表不可以修改

# 列表和元组可以相互转换，通过list()和tuple()函数
# info_tuple[1] = "mm" # 元组不支持修改，会报错
info_list = list(info_tuple)
info_list[1] = "mm"
print(info_list)
