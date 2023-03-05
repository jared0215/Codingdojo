# BASIC
for x in range(151):
    print(x)

# Multiples of Five
for i in range(5,1005):
    if i % 5 == 0:
        print(i)

# Counting, the Dojo Way
for a in range(1,105):
    if a % 10 == 0:
        print(a, 'Coding Dojo')
    elif a % 5 == 0:
        print(a, 'Coding')
    else:
        print(a)

# Woah. That Sucker's Huge
sum = 0
for b in range(1, 500001, 2):
    sum += b
    print(sum)