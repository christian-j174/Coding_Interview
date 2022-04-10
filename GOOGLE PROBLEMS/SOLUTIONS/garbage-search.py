"""

This is the problem that we used in the group mock interview session on Dec 11:

Write a function which accepts two strings as arguments and returns True/False
depending on whether the second string exists within the first string. However, in general the first string will contain a lot of garbage characters that we don't care about,
 and we need to sift through the garbage. Specifically, we want to return True if, by removing some combination of
 characters from the first string, we can make what remains equal to the second string. Examples:

F('a!b!c', 'abc') == True
F('azozbaz', 'zz') == True
F('abc','cba') == False

"""

# def Shirley(large,small):
#     i = 0
#     for ch in small:
#         while i < len(large) and ch != large[i]:
#             i += 1
#             if i == len(large):
#                 return False
#     return True

# def Manson(large,small):
#     i = 0
#     for ch in large:
#         if ch == small[i]:
#             i += 1
#             if i == len(small):
#                 return True
#     return False