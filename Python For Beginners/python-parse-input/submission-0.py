from typing import List

def read_integers() -> List[int]:
    user_input = input("")
    list_input = user_input.split(",")
    for i,j in enumerate(list_input):
        list_input[i] = int(j)
    return list_input

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
