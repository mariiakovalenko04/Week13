def findMaxInList(numbers):
    maxValue = 0
    for number in numbers:
        if number > maxValue:
            maxValue = number
    return maxValue

my_List = [1, 10, 10, 8]
biggest_Number = findMaxInList(my_List)
print (biggest_Number)
