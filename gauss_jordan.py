# the boner
# augmented_matrix = a_m
# https://www.perplexity.ai/apps/b435a2e5-725f-439c-b24a-6892fc21b774 >> visual link

def gauss_jordan(a_m):
    n = len(a_m)
    print(n)

    for i in range(n):
        print(i)

        # swap
        # row swapping
        for k in range(i + 1, n):
            if a_m[k][i] != 0:
                a_m[i], a_m[k] = a_m[k], a_m[i]
                # print("##")
                # print(a_m[i], a_m[k])
                # print("##")
                break
        
        # leading one
        pivot = a_m[i][i]
        for j in range(n + 1):
            a_m[i][j] /= pivot
        
        print("###########")
        print(k) 
        print("###########")
        # rest column 0
        for k in range(n):
            if k != i:
                factor = a_m[k][i]
                for j in range(n + 1):
                    a_m[k][j] -= factor * a_m[i][j]
    
    
    # Extract solutions from last column
    return [row[n] for row in a_m]


# the matrix
A = [[90, -30, -50, 0, 20],
     [-30, 150, 0, -60, 0],
     [-50, 0, 230, -30, -30],
     [0, -60, -30, 220, 40]]


solutions = gauss_jordan(A)
print("Solutions (x, y, z):", solutions)
print("RREF matrix:\n", A)