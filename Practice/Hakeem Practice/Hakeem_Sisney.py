students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(students):
    for i in students:
        for key, val in i.items():
            print(key, "-", val)


iterateDictionary(students)


def iterateDictionary(students):
    for i in students:
        for key in i.keys():
            for val in i.values():
                print(key, "-", val)


iterateDictionary(students)


# ('first_name', "-", x['first_name'] +
#               ",", 'last_name', "-", x['last_name'])
