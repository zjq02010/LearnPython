# 字符串的常用基本操作
# 使用单引号''或者双引号""(常用)定义
str1 = "今天天气真好！"
for i in str1:
    print(i)

# 统计字符串长度
print(len(str1))
# 统计某个字符出现的次数
print(str1.count("天"))
# 统计子串出现的位置
print("子串出现的位置：", str1.index("天"))
# str1[-1] = "?"
print(str1)

# 字符串的全部方法
# In [3]: hello_str = ""
# In [4]: hello_str.
# hello_str.capitalize    hello_str.isalnum
#     hello_str.join          hello_str.rsplit
# hello_str.casefold      hello_str.isalpha
#     hello_str.ljust         hello_str.rstrip
# hello_str.center        hello_str.isdecimal
#   hello_str.lower         hello_str.split
# hello_str.count         hello_str.isdigit
#    hello_str.lstrip        hello_str.splitlines
# hello_str.encode        hello_str.isidentifier
#  hello_str.maketrans     hello_str.startswith
# hello_str.endswith      hello_str.islower
#      hello_str.partition     hello_str.strip
# hello_str.expandtabs    hello_str.isnumeric
#   hello_str.replace       hello_str.swapcase
# hello_str.find          hello_str.isprintable
#  hello_str.rfind         hello_str.title
# hello_str.format        hello_str.isspace
#     hello_str.rindex        hello_str.translate
# hello_str.format_map    hello_str.istitle
#     hello_str.rjust         hello_str.upper
# hello_str.index         hello_str.isupper
#    hello_str.rpartition    hello_str.zfill

# 字符串的切片slice
# 切片采用区间的形式，左闭右开[index_start:index_end:step]
str2 = "1234567"
str3 = str2[2::2]
print(str3)
