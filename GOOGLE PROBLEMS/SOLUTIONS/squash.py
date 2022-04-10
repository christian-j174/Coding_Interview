"""
This is the problem that we used in the group mock interview session on Dec 13:

We wish to perform the following transformation on a string: Whenever an uppercase and a lowercase version of the same letter are adjacent to each other, the one which appears second is removed from the string. This process repeats until nothing else may be removed. If multiple removals are possible at the same time they must all be performed, so for example 'aAa' would become 'a'.

Write a function called Squash() which takes a string as its only argument, performs the above transformation upon it, and returns the resulting string.

‘Aa’ -> ‘A’
‘aA’ -> a
‘bzBbq’ -> ‘bzBq’
‘SS’ -> ‘SS’
‘Aaaaaaaaaaaaaa’ -> ‘A’
'AaaaaAa' -> ‘Aaaa’ -> ‘Aaa’ -> ‘Aa’ -> ‘A’

Addendum: This problem can be solved either iteratively or recursively - try to make both ways work.


"""


def Squash1(s):
    out = ''
    for i in range(len(s)-1, 0, -1):
        c1 = s[i-1]
        c2 = s[i]
        if c1.lower() != c2.lower() or c1 == c2:
            out = c2 + out
    return s[0] + out

def Squash(s):
    prev = None
    while prev != s:
        prev = s
        s = Squash1(s)
    return s