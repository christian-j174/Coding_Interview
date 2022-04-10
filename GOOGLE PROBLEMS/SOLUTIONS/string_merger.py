"""
You are given two strings. One contains some random assortment of uppercase letters,
the other contains some random assortment of lowercase letters. Both strings are sorted in alphabetical order.
Write a function which takes both strings as arguments and returns a new string that is the result of merging them
such that alphabetical order is preserved and
uppercase versions of any given letter appear before the lowercase versions. Example:

str1 = "AACFMMQYZ"
str2 = "abefgqqrsxyz"

result = "AAabCeFfgMMQqqrsxYyZz"

"""

# def Merge(uppers,lowers):
#     out = ''
#     iu = il = 0
#     while iu < len(uppers) and il < len(lowers):
#         uu = uppers[iu]
#         ll = lowers[il]
#         if uu.lower() <= ll:
#             out += uu
#             iu += 1
#         else:
#             out += ll
#             il += 1
#     return out + uppers[iu:] + lowers[il:]