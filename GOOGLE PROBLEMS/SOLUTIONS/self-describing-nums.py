"""
This is the problem that we used in the group mock interview session on Dec 14:

An integer is said to be "self-describing" if it has the property that, when digit positions are labeled 0 to N-1, the digit in each position is equal to the number of times that digit appears in the number.

For example, 2020 is a four-digit self-describing number:

  position 0 has value 2 and there are 2 0s
  position 1 has value 0 and there are 0 1s
  position 2 has value 2 and there are 2 2s
  position 3 has value 0 and there are 0 3s

1210 is another four-digit self-describing number.
6210001000 is a ten-digit self-describing number.
Note that all self-describing numbers must contain ten or fewer digits.

Write a generator that returns all self-describing numbers in ascending order.

Reference: https://rosettacode.org/wiki/Self-describing_numbers


"""


# def isSDN(n):
#     s = str(n)
#     z = [0] * 10
#     for d in s:
#          z[int(d)] += 1
#     for i in range(len(s)):
#         if z[i] != int(s[i]): return False
#     return True
#
# def SDN():
#     for i in range(10 * 1000 * 1000 * 1000):
#         if isSDN(i): yield i


# The solution I had written:
# def SelfDescribingIntegerChecker(itg):
#     itg = str(itg)
#     for dgt in range(len(itg)):
#         if int(itg[dgt]) != itg.count(str(dgt)):
#             return False
#     return True
#
# def Count2(it2, dg2):
#     tms = 0
#     for val in it2:
#         if int(val) == dg2:
#             tms += 1
#     return tms
#
# #No .count() version
# def SelfDescribingIntegerChecker(itg_int):
#     itg_str = str(itg_int)
#     for dgt in range(len(itg_str)):
#         if int(itg_str[dgt]) != Count2(itg_str, dgt):
#             return False
#     return True
#
# BILLION = 1000*3
#
# def SelfDescribingIntegerGenerator():
#     for i in range(10BILLION):
#         if SelfDescribingIntegerChecker(i):
#             yield i
#
# for i in SelfDescribingIntegerGenerator():
#     print(i)