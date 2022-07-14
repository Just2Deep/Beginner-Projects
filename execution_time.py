# Execution Time of a Python Program

from time import time

start = time()

# Python program to create acronyms
word = "Artificial Intelligence is the future of technology"
text = word.split()
a = ""

for i in text:
    a = a+str(i[0]).upper()

print(a)

end = time()

execution_time = end-start

print('Execution time in seconds ', execution_time)
