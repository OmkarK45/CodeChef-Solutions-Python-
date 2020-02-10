t = int(input())

for i in range(t):
    # s =0 
    n = int(input())
    if n>9:
        last_digit = n%10
        first_digit = n        
        while(first_digit >= 10):
            first_digit = first_digit // 10
    print(first_digit + last_digit)            