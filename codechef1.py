 # amount pooja want to withdraw 
 # pooja's initial bank account 
# # z = 0
# import math
# def accept_event():
#     x,y = map(float,raw_input().split())
#     if x%5 == 0:
#         if y > x:
#             y = y - x - 0.50
#             print("{0:.2f}".format(y))
#         elif y<x:
#             print("{0:.2f}".format(y))    
#             # print("available balance : ", y)
#     elif x%5 != 0:
#         print("{0:.2f}".format(y))

# accept_event()        
x,y = map(float, input().split())
if x%5 == 0:
    if y > x:
        y = y - x - 0.50
        print("{0:.2f}".format(y))
    elif y<x:
        print("{0:.2f}".format(y))    
elif x%5 != 0:
    print("{0:.2f}".format(y))
