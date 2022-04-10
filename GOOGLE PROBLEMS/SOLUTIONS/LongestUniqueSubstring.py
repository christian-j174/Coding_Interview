"""
Write a function called LongestUniqueSubstring() which takes a non-empty string and
returns its longest continuous substring which contains no duplicate characters. If there are multiple such substrings,
return the one which appears earliest.

Examples:

LongestUniqueSubstring('abcbdef')                        cbdef
LongestUniqueSubstring('aabbccddefghhii')        defgh
LongestUniqueSubstring('Yarrrrrrrr!')                    Yar
LongestUniqueSubstring('aaaaaa')                          a
LongestUniqueSubstring('spam+spam+spam+sausage+eggs+spam')        usage+

"""


# def LongestUniqueSubstring(A):
#     out = tmp = ''
#     for a in A:
#         idx = tmp.find( a )
#         if idx > -1:
#             tmp = tmp[idx + 1:]
#         tmp += a
#         if len( out ) < len( tmp ):
#             out = tmp
#     return out


# def LongestUniqueSubstring(s):
#     lus = None
#     for i in range(len(s)):
#         tl = ''
#         for j in range(i,len(s)):
#             if not s[j] in tl:
#                 tl += s[j]
#             else:
#                 break
#         if lus == None or len(tl) > len(lus):
#             lus = tl
#     return lus