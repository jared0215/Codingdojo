# 1. Countdown
newList = []
def countdown(number):
    while number > -1:
        newList.append(number)
        number -= 1
    return newList
print(countdown(5))

# 2. Print and Return
def print_and_return(testList = []):
    print(testList[0])
    return testList[1]
print_and_return([17,38])

# 3. First Plus Length
def first_plus_length(ourList = []):
    return len(ourList) + ourList[0]
print(first_plus_length([1,2,3,4,5]))

# 4. Values Greater Than Second
newValueList = []
def values_greater_than_second(valueList = []):
    if len(valueList) < 2:
        return False
    for x in range(len(valueList)):
        if valueList[x] > valueList[2]:
            newValueList.append(valueList[x])
    return newValueList

values_greater_than_second([1,2,3,4,5,6,7,8])
print(newValueList)
print(len(newValueList))

# 5. This Length, That Value
def this_length_that_value(size = 0, value = 0):
    thisList = []
    for x in range(size, 0, -1):
        thisList.append(x)
    for y in range(len(thisList)):
        thisList[y] = value
    return thisList

print(this_length_that_value(6, 2))