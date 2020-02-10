t = int(input())

# def sumdigit(int):
#     while(p>0):
#         r = p%10
#         sum = sum +r
#         p = p//10
#     print(p)  

# for tc in range(t):
#     p = int(input())
#     sumdigit(p)    

for i in range(t):
    s =0 
    n = int(input())
    if n>9:
        while n>0:
            r = n%10
            s = s+r
            n = n//10
        print(s)        
