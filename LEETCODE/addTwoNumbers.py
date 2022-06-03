# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1, l2:
#         result = []
#         l1 = l1.reverse()
#         l2 = l2.reverse()
#         number1 = ''
#         number2 = ''
#         for i in l1:
#             number1 += str( i )
#
#         for ii in l2:
#             number2 += str( ii )
#
#         number1 = float( number1 )
#         number2 = float( number2 )
#
#         r = number1 + number2
#
#         for iii in str( r ):
#             result.append( int( iii ) )
#
#         return result