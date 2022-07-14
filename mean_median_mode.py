# Mean Median and Mode using Python

# Mean

list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean = sum(list1)/len(list1)
print('Mean:', mean)

# Median

# when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
# when the total number of values is odd: Median = {(n+1)/2}th term

list2 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list2.sort()

if len(list2) % 2 != 0:
    median_idx = (len(list2)+1)//2
    median = list2[median_idx]
else:
    median_idx1, median_idx2 = len(list2)//2, len(list2)//2 + 1
    median = (list2[median_idx1] + list2[median_idx2])//2

print('Median:', median)

# Mode
# Mode is the most frequently occurring value among all the values.

list3 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}

for i in list3:
    frequency.setdefault(i, 0)
    frequency[i] += 1

frequent = max(frequency.values())

for key, value in frequency.items():
    if value == frequent:
        mode = key

print('Mode:', mode)
