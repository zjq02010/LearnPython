# 字典采用键值对的形式，储存一个物体的相关信息
# 通常将多个字典放入一个列表中，进行遍历操作
card_list = [
    {
        "name": "zjq",
        "age": 18,
        "gender": "Man"
    },
    {
        "name": "mm",
        "age": 18,
        "gender": "Woman"
    }
]

print(card_list)
for card in card_list:
    print(card)
card_list[1]["age"] = 20
print(card_list)
