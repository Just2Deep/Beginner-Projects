# Find prime number or return only prime numbers in a given range

num = 17
low = 3
high = 30

for i in range(2, num):
    if num % i == 0:
        print('Not Prime')
        break
else:
    print("Prime")

for i in range(low, high+1):
    for n in range(2, i):
        if i % n == 0:
            print(f'{i} Not Prime')
            break
    else:
        print(f"{i} Prime")
