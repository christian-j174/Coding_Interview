"""This is the problem that we used in the group mock interview session on Dec 9:

Write a function which takes as its only argument a string containing some combination of parentheses and/or
square bracket characters, and return True/False depending on whether those characters are balanced.
The string is said to be balanced if every '(' has a matching ')' and every '[' has a matching ']', and vice-versa.
Matched pairs may only contain other matched pairs within them.

Examples:

'' True
'()' True
'[]' True
'(())' True
'()()' True
'[()]' True
'(' False
')(' False
'[(])' False
'()))' False


"""


# def F(s):
#     prev = None
#     while prev != len(s):
#         prev = len(s)
#         s = s.replace('()','')
#         s = s.replace('[]','')
#     return len(s) == 0


#
# def parenthesis(string):
#     while True:
#         if len(string) <= 2:
#             break
#         if “()” in string:
#             string.remove(“()”)
#         elif “[]” in string:
#             string.remove(“[]”)
#         else:
#             return False
#     if string != “()” or string != “[]”:
#         return False
#     return True