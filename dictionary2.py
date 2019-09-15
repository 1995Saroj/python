# This is a Python Program that concatenates the dictionaries to create a new one

dic1 = {
    1: 10,
    2: 20
    } 
dic2 = {
    3: 30,
    4: 40
    } 
dic3 = {
    5: 50,
    6: 60
    }
dic4 = {}
for dic in (dic1, dic2, dic3):
    dic4.update(dic)
print("The new obtained Dictionary is: ",dic4)
