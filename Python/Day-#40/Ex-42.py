"""
Question: Print out in each line the sum of homologous items of the two sequences.

a = [1, 2, 3]
b = (4, 5, 6)

Expected output: 

5
7
9
"""

a = [1, 2, 3]
b = (4, 5, 6)

for i,j in zip(a,b):
    print(i + j)

print(list(zip(a,b)))
# [(1, 4), (2, 5), (3, 6)]