# Row vector
row = [1, 2, 3]
# Column vector
col = [[1], [2], [3]]
# Matrix
A = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
print("Row:", row)
print("Column:", col)
print("Matrix:", A)

rows = len(A)
cols = len(A[0])
print(A[0])
print("Dimension:", rows, "x", cols)
# Square matrix check
if rows == cols:
    print("Square Matrix")
# Identity matrix check
identity = True
for i in range(rows):
    for j in range(cols):
        if (i == j and A[i][j] != 1) or (i != j and A[i][j] != 0):
            identity = False

if (identity == False):
    print("not identity")
else:
    print("identity it is")
# i liked this type of syntax everything is just so worst

# Simple check: count non-zero rows
rank = 0
for row in A:
    for val in row:
        if val != 0:
            rank += 1
print("rank=", rank)
