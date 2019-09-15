# This is a Python Program that merge two dictionaries

dic1 = {
    1: "a",
    2: "b",
    3: "c"
}

dic2 = {
    4: "a",
    5: "b",
    6: "c"
}
dic = dic1.copy()
dic.update(dic2)
print(dic)