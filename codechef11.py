t = int(input())

for i in range(t):
    val = []
    val= list(map(int,input().split(" ")))
    val.sort()
    print(val[1])