import random

def BubbleSort(A, n):
    for i in range(0, n):
       for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
    return A


A = []
s = random.randint(5, 100)
for i in range(0, s):
    A.append(random.randint(0, 1000))

A = BubbleSort(A, len(A))

print "Now displaying Bubble."
print A