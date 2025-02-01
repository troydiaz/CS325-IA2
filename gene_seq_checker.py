import numpy
import sys
from check_cost import read_cost_matrix

# Import from file to arrays A, B




def edit_distance(A, B, loss_matrix): 
    m = len(A)
    n = len(B)
    Edit = [[n] for i in range [0,m]]
    ptr = numpy.zeros((m, n))
    Edit[0, 0] = loss_matrix[1, 1]
    for j in range[1, n + 1]:
        Edit[0, j] = loss_matrix[1, x_indexdict.B[j - 1]]
    for i in range [1, m + 1]:
        Edit[i, 0] = loss_matrix[y_indexdict.A[i - 1], 1]

    for i in range [1, m + 1]:
            insert = Edit[i, j - 1] + loss_matrix[1, x_indexdict.B[j - 1]]
            delete = Edit[i - 1, j] + loss_matrix[y_indexdict.A[i - 1], 1]
            replace = Edit[i - 1, j - 1] + loss_matrix[y_indexdict.A[i - 1], x_indexdict.B[j - 1]]
            Edit[i, j] = min(insert, delete, replace)
            ptr[i, j] = numpy.argmin([insert, delete, replace])
            # ptr[i,j] stores operation used to reach [i, j]:  0 for insert, 1 for delete, 2 for replace
    return Edit, ptr

def cost_index(letter) -> int:
    for i in range[1, m + 1]:
        if C[0][i] == letter:
            return i

def main(argv):
    print('_' * 100)

    # Default file paths
    costfile = 'imp2cost.txt'
    outputfile = 'imp2output.txt'  # The primary solution file
    second_outputfile = ''         # optional second solution file
    log_results = 'cost_check_results.txt'

    loss_matrix, x_indexdict, y_indexdict = read_cost_matrix(fns=costfile)
    log_results = 'cost_check_results.txt'
if __name__ == "__main__":
    main(sys.argv[1:])