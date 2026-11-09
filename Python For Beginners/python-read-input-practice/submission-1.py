def add_two_numbers() -> int:
    user_input = input()
    user_list = user_input.split(",")
    sum = int(user_list[0]) + int(user_list[1])
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
