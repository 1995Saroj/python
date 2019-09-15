# This is a Python Program that checks if a given key already exists in a dictionary or not

dic1 = {
    1: "a",
    2: "b",
    3: "c"
}
def present(num):
    if num in dic1:
        print("Yes, The key is present.")
    else:
        print("No, They key is not present.")
present(1)
present(9)