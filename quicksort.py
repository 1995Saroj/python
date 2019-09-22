def quicksort(nums):
    if len(nums) <= 1:
        return nums
    smaller = []
    equal = []
    larger = []
    pivot = nums[0]
    for x in nums:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quicksort(smaller) + equal + quicksort(larger)

print(quicksort([3,1,0,3,9,7,8,2]))