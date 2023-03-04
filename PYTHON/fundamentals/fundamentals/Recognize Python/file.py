num1 = 42       # variable declaration, data types, primitive, numbers, initialize integer
num2 = 2.3      # variable declaration, data types, primitive, numbers, initialize float
boolean = True          # variable declaration, data types, primitive, initialize boolean
string = 'Hello World'      # variable declaration, data types, primitive, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']      # variable declaration, composite, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}      # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana')       # variable declaration, initialize tuple
print(type(fruit))      # function, argument, built-in function, type check, argument
print(pizza_toppings[1])        # function, argument, list, access value
pizza_toppings.append('Mushrooms')      # function, list, add value
print(person['name'])     # function, dictionary, access value
person['name'] = 'George'       # dictionary, change value
person['eye_color'] = 'blue'        # dictionary, add value
print(fruit[2])            # function, argument, tuple, access value

if num1 > 45:       # conditional, if statement
    print("It's greater")   # function, print string
else:                    # conditional, else statement
    print("It's lower")         # function, print string

if len(string) < 5:          # conditional, if statement, function, legnth check, argument
    print("It's a short word!")         # function, print string
elif len(string) > 15:      # conditional, else if statement, function, legnth check, argument
    print("It's a long word!")       # function, print string
else:               # conditional, else statement
    print("Just right!")        # function, print string

for x in range(5):      # for loop, built-in function, stop
    print(x)        # function, print variable

for x in range(2,5):        # for loop, built-in function, start, stop
    print(x)        # function, print variable

for x in range(2,10,3):     # for loop, built-in function, start, stop, step (increment)
    print(x)        # function, print variable

x = 0       # variable declaration, numbers, integer
while(x < 5):        # while loop, start, stop
    print(x)        # function, print variable
    x += 1      # variable declaration, increment 


pizza_toppings.pop()         # function, removes last value from list
pizza_toppings.pop(1)       # function, removes value from specified position

print(person)       # function, print variable
person.pop('eye_color')     # function, removes key from dictionary
print(person)    # function, print variable

for topping in pizza_toppings:    # conditional, for loop, variable iterates through list, start
    if topping == 'Pepperoni':      # if statement, variable topping is equal to 'Pepperoni'
        continue        # continue to next topping
    print('After 1st if statement') # function, print string
    if topping == 'Olives': # conditional if statement, variable topping is equal to 'Olives'
        break # break, terminates loop, (stop i think?)

def print_hello_ten_times():        # define function
    for num in range(10):       # for loop, built-in function, stop
        print('Hello')      # function, print string

print_hello_ten_times()         # call function
def print_hello_x_times(x):     # define function, argument, variable
    for num in range(x):        # for loop, built-in function, variable, stop
        print('Hello')      # function, print string

print_hello_x_times(4)       # call function, argument, variable

def print_hello_x_or_ten_times(x = 10):     # define function, argument, variable declaration
    for num in range(x):        # for loop, built-in function, argument, variable, stop
        print('Hello')      # function, print string

print_hello_x_or_ten_times()        # call function
print_hello_x_or_ten_times(4)       # call function, argument, variable


"""
Bonus section
"""

# print(num3)      # ! - NameError: name <variable name> is not defined

# num3 = 72        # ! - variable declaration, has no output

# fruit[0] = 'cranberry'        # ! - TypeError: 'tuple' object does not support item assignment

# print(person['favorite_team'])      # ! - KeyError: 'favorite_team'

# print(pizza_toppings[7])      # ! - IndexError: list index out of range

#   print(boolean)        #! - IndentationError: unexpected indent

# fruit.append('raspberry')      # ! - AttributeError: 'tuple' object has no attribute 'append'

# fruit.pop(1)      # ! - AttributeError: 'tuple' object has no attribute 'pop'