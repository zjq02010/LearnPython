nameList = ["mm1", "mm2", "mm3"]
print(nameList)
# append
nameList.append("zjq")
print(nameList)
# count
print(nameList.count("mm2"))
# extend
addList = ["zjq", 666]
nameList.extend(addList)
print(nameList)
# index
name_Index = nameList.index("zjq")
print(name_Index)
# insert
nameList.insert(1, "zzjjqq")
print(nameList)
# pop
print(nameList.pop(6))
print(nameList)
# remove
nameList.remove("mm2")
print(nameList)
# reverse
nameList.reverse()
print(nameList)
# sort
nameList.sort()
print(nameList)

# for循环遍历 iteraiton
for name in nameList:
    print("My name is ", name)
