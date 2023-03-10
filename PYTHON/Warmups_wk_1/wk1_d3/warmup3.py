my_list = [
    {'id': '1', 'fname': 'bob'},
    {'id': '6', 'fname': 'mike'},
    {'id': '4', 'fname': 'stacy'}
]


def warmUp(my_list):
    for x in my_list:
        if x['id'] == '4':
            x['fname'] = 'sarah'
            print(my_list)
    return my_list


warmUp(my_list)
