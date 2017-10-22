my_list = [-7, 0, 1,2,3,4,5,6,7,8,9,10,11,12,13,55]

index = 0

while index < len(my_list):
    if my_list[index] == 1:
        print("January")
    elif my_list[index] == 2:
        print("February")
    elif my_list[index] == 3:
        print("March")
    elif my_list[index] == 4:
        print("April")
    elif my_list[index] == 5:
        print("May")
    elif my_list[index] == 6:
        print("June")
    elif my_list[index] == 7:
        print("July")
    elif my_list[index] == 8:
        print("August")
    elif my_list[index] == 9:
        print("September")
    elif my_list[index] == 10:
        print("October")
    elif my_list[index] == 11:
        print("November")
    elif my_list[index] == 12:
        print("December")
    else:
        print("Number not valid")

    index = index + 1