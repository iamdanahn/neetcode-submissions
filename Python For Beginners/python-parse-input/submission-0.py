from typing import List

def read_integers() -> List[int]:
    str_list = input().split(",")
    res = []
    for el in str_list:
        res.append(int(el))
    return res

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
