# def demo(a, b, *c):
#     print(a)
#     print(b)
#     print(c)
#     return a+b, a*b
# def sum_numbers(num):
#     print(num)
#     if num ==1:
#         return
#     sum_numbers(num-1)

# sum_numbers(3)
# print("Hello World")
# print("MM")
# x2 = demo(2, 6)
# print(x2)
# print(type(x2))
# a = 1
# b = 3
# print(a, b)
# # python 专属解法，交换值
# b,a = (a, b)
# b,a = a, b #等号右边是元组，只不过省略了括号
# demo(1, 2, 3, 36, 5, 4)


# 递归求和
def sum(num):
    """
    递归求和练习
    """
    # 1. 确定出口,否则会死循环
    if num == 1:
        return 1
    # 2. 数字的累加 num + (num-1,...+ 1)
    #    假设sum()能正确处理(num-1,...+ 1)
    temp = sum(num-1)
    #    相加
    return num + temp


print(sum(100))
print("Hello")