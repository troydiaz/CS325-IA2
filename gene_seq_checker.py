import numpy

# Import cost matrix into array C

def edit_distance(A, B, C): 
    m = len(A)
    n = len(B)
    Edit = [[n] for i in range [0,m]]
    ptr = numpy.zeros((m, n))
    Edit[0, 0] = C[1, 1]
    for j in range[1, n + 1]:
        Edit[0, j] = C[1, costIndex(B[j - 1])]
    for i in range [1, m + 1]:
        Edit[i, 0] = C[costIndex(A[i - 1]), 1]

    for i in range [1, m + 1]:
            insert = Edit[i, j - 1] + C[1, costIndex(B[j - 1])]
            delete = Edit[i - 1, j] + C[costIndex(A[i - 1]), 1]
            replace = Edit[i - 1, j - 1] + C[costIndex(A[i - 1]), costIndex(B[j - 1])]
            Edit[i, j] = min(insert, delete, replace)
            ptr[i, j] = numpy.argmin([insert, delete, replace])
            # ptr[i,j] stores operation used to reach [i, j]:  0 for insert, 1 for delete, 2 for replace
    return Edit, ptr

def cost_index(letter: char) -> int:
    for i in range[1, m + 1]:
        if C[0][i] == letter:
            return i