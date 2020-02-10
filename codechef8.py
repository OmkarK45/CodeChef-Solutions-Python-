t  = int(input())
mylist = []

for i in range(t):
    count = 0
    n = int(input())
    res = [int(x) for x in str(n)]
    count = res.count(4) 
    print(count)    