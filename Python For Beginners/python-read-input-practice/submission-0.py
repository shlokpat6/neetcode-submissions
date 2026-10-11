def add_two_numbers() -> int:
    user_input = input("")
    list_input = user_input.split(",")
    for i,j in enumerate(list_input):
        list_input[i] = int(j)
    return list_input[0] + list_input[1]



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
