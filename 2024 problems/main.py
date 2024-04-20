
"""
Why?
Execution Plan?
"""

#Problem 1
"""
Write a function get_middle_char(s) that takes a string
s as input and returns the middle character(s) of the string,
or an empty string if the length of the input string is even.
"""

def get_middle_char(s):
    string_size = len(s)
    if(string_size == 0 or (string_size % 2 == 0)):
        return ""
    else:
        middle_position = string_size // 2
        return s[middle_position]





def main():
    print(get_middle_char("hello")) # return "l"
    return 0

if __name__ == "__main__":
    main()
