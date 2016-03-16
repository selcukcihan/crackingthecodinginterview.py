#! /usr/bin/env python
"""
"""

def remove_duplicate_characters(input_string):
    str_array = list(input_string)
    str_array.append('\0')
    cur = 1
    end = len(input_string)
    while cur < end:
        for i, c in enumerate(str_array[0:cur]):
            if c == str_array[cur]:
                while str_array[end - 1] == str_array[cur] and cur < end:
                    str_array[end - 1] = '\0'
                    end = end - 1
                if cur < end:
                    str_array[cur] = str_array[end - 1]
                    str_array[end - 1] = '\0'
                    end = end - 1
                    cur = cur - 1
                break

        cur = cur + 1
    return "".join(str_array)
       
def test_run():
    for s in ["bilgisayar", "", "a", "aaaa", "aabb"]:
        print s + "\t" + remove_duplicate_characters(s)



