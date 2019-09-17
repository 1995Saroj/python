def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if target == nums[mid]:
            found = True
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if found == True:
        return mid
    else:
        return -1
a = [1,2,3,4,5]
b = 9
print(binarySearch(a,b))