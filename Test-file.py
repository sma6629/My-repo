def swap(alist, i, j):
    temp = alist[i]
    alist[i] = alist[j]
    alist[j] = temp

import random
def bubble_sort(alist):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(alist)-1):
            if alist[i] > alist[i+1]:
                sorted = False
                swap(alist, i, i+1)

alist = [random.randint(0, 101) for i in range(20)]
#alist = [314, 1, 3, 10, 3, 5]
print(alist)
bubble_sort(alist)
print(alist)

def binary_search(alist, value):
    while len(alist) > 0:
        midpoint = (len(alist) - 1) // 2
        if alist[midpoint] == value:
            return value
        elif value < alist[midpoint]:
            alist = alist[:midpoint]
        elif value > alist[midpoint]:
            alist = alist[midpoint+1:]
    return "Value was not found"

l = [i for i in range(1, 10000)]
#print(binary_search(l, 8889))

def sequential_search(alist, value):
    for i in range(len(alist)):
        if alist[i] == value:
            return value

    return "Value was not found"

#print(sequential_search(l, 88889))

def fib(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*fib(n-1)
print(fib(45))