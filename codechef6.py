# sort numbers in increasing order Python 

t = int(input())
mylist = []

for i in range(t):
    p = int(input())
    mylist.append(p)
    p = 0
mylist.sort()

# r = mylist.len()
for i in range(t):
    print(mylist[i], end="\n")