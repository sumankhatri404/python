'''''raise exeception '''

# import sys
#
# randsys = ['a', 0, 2]
# for n in randsys:
#
#     try:
#         print("the entry is {}".format(n))
#         r = 1 / int(n)
#         break
#
#     except:
#           print("error", sys.exc_info()[0], "occured")
#           print("next entry")
# print("the entry is {} and {}".format(n, r))
#

import sys

# randSys=['a',0,2]
#
# for n in randSys:
#     try:
#         print("the entry is {}".format(n))
#         r=1/int(n)
#         break
#     except Exception as e:
#         print("error",e.__class__)
# print("the reciporcal is {} and {}".format(n,r))


'''Raising Exceptions in Python'''

# try:
#     a=int(input("enter a number = "))
#     if a<=0:
#         raise ValueError("the number is not positive ")
#
# except ValueError as ve:
#     print(ve)


''''user defined exceptions'''


# class ValueTooBig(Exception):
#     pass
#
#
# class ValueTooSmall(Exception):
#     pass
#
#
# numbers = 40
#
# while True:
#     try:
#         num=int(input("enter a number ="))
#         if num < numbers:
#             raise ValueTooSmall
#         elif num > numbers:
            raise ValueTooBig
        break
    except ValueTooSmall:
        print("The value is too small !guess again")
    except ValueTooBig:
        print("The given value is too large !guess again")
print("congratulations you guess correctly")


