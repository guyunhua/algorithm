# -*- coding:utf8 -*-
import random
#插入排序 每次遍历 将当前值插入到前面的列表中

def InsertionSort(A, n):
    for j in range(1, n):
        key = A[j]

        i = j -1
        while i >=0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


A = []
s = random.randint(5, 100)
for i in range(0, s):
    A.append(random.randint(0, 1000))

A = InsertionSort(A, len(A))

print "Now displaying InsertSort."
print A

