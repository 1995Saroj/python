# This is a Python Program that sort a list of numbers using Insertion Sort technique
def insertionSort(nums):
    for index in range(1, len(nums)):
        number = nums[index]
        i = index
        while i > 0 and number < nums[i - 1]:
            nums[i] = nums[i - 1]
            i += -1
        nums[i] = number
    return nums

print(insertionSort([5,1,9,0,8,2,6,2]))