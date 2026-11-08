def remove_fourth_character(word: str) -> str:
    mod_string1 = word[:3]
    mod_string2 = word[4:]
    return mod_string1 + mod_string2


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
