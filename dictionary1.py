# This is a Python Program that sorts a dictionary by its value

import operator
dict = {
    4: 'a',
    1: 'b',
    3: 'c',
    2: 'd',
    5: 'e'
}

print("Original Dictionary: ",dict)
sortedAscending = sorted(dict.items(), key = operator.itemgetter(0))
print("Dictionary in Ascending Order by value is: ",sortedAscending)

sortedDescending = sorted(dict.items(), key = operator.itemgetter(0), reverse = True)
print("Dictionary in Descending Order by value is: ",sortedDescending)