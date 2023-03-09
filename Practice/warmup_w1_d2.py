my_list = ["oranges", "apples", "grapes", "bananas", "celery"]
def fruits(my_list):
    for x in range(len(my_list)):
        if my_list[x] == "celery":
            my_list[x] = "pineapple"
            print("COMPLETE")
    return my_list
fruits(my_list)