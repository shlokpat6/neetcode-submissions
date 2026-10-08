from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    dict_word = {}
    for i in word:
        if i not in dict_word:
            dict_word[i] = 1
        else:
            dict_word[i] +=1

    return dict_word




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
