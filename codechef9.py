#  reverse of a number python ! 

t = int(input())

# def rev_fun(x):
#     rev = 0
#     while x>0:
#         a = x%10
#         rev = (rev*10) + x
#         x = x//10
#     print(rev)

for i in range(t):
    n = int(input())
    rev = 0
    while n>0:
        a = n%10
        rev = (rev*10) + a
        n = n//10
    print(rev)     