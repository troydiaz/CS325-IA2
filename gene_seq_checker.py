import numpy
import sys
from check_cost import read_cost_matrix, gen_matrix

def edit_distance(A, B, loss_matrix, x_indexdict, y_indexdict): 
    m = len(A)
    n = len(B)
    Edit = numpy.zeros((m + 1, n + 1))
    ptr = numpy.zeros((m + 1, n + 1))
    Edit[0, 0] = loss_matrix[1][1]
    for j in range(1, n + 1):
        Edit[0][j] = loss_matrix[1][x_indexdict[B[j - 1]]]
        ptr[0][j] = 0
    for i in range (1, m + 1):
        Edit[i][0] = loss_matrix[y_indexdict[A[i - 1]]][1]
        ptr[i][0] = 1

    for i in range (1, m + 1):
        for j in range (1, n + 1):
            insert = Edit[i][j - 1] + loss_matrix[1][x_indexdict[B[j - 1]]]
            delete = Edit[i - 1][j] + loss_matrix[y_indexdict[A[i - 1]]][1]
            replace = Edit[i - 1][j - 1] + loss_matrix[y_indexdict[A[i - 1]]][x_indexdict[B[j - 1]]]
            operations = [insert, delete, replace]
            operation = numpy.argmin(operations)
            ptr[i][j] = operation
            Edit[i][j] = operations[operation]
            # ptr[i,j] stores operation used to reach [i, j]:  0 for insert, 1 for delete, 2 for replace
    return Edit[m][n], ptr
        
def backtrack_alignment(A, B, ptr, m, n):
    aligned_seqA, aligned_seqB = [], []
    i, j = m, n
    
    while i > 0 or j > 0:
        if ptr[i][j] == 2:
            aligned_seqA.append(A[i-1])
            aligned_seqB.append(B[j-1])
            i, j = i-1, j-1
        elif ptr[i][j] == 1:
            aligned_seqA.append(A[i-1])
            aligned_seqB.append('-')
            i = i-1
        else:
            aligned_seqA.append('-')
            aligned_seqB.append(B[j-1])
            j = j-1
    
    # Return the reversed aligned sequences
    return ''.join(reversed(aligned_seqA)), ''.join(reversed(aligned_seqB))

def read_sequences(inputfile):
    # Reads Input Fie
    with open(inputfile, 'r') as file:
        return [line.strip().split(',') for line in file]

def write_output(alignments, outputfile):
    # Writes alignment result to imp3output.txt (we can change the naming later)
    with open(outputfile, 'w') as file:
        for seq1, seq2, cost in alignments:
            file.write(f"{seq1},{seq2}:{cost}\n")

def compute_alignment(A, B, loss_matrix, x_indexdict, y_indexdict):
    cost, ptr = edit_distance(A, B, loss_matrix, x_indexdict, y_indexdict)
    alignment = backtrack_alignment(A, B, ptr, len(A), len(B))
    return alignment[0], alignment[1], cost

def main(argv):
    print('_' * 100)

    # Default file paths
    inputfile = 'imp2input.txt'
    costfile = 'imp2cost.txt'
    outputfile = 'imp2output.txt'  # The primary solution file
    second_outputfile = ''         # optional second solution file
    log_results = 'cost_check_results.txt'

    loss_matrix, x_indexdict, y_indexdict = read_cost_matrix(fns=costfile)
    
    sequences = read_sequences(inputfile)
    alignments = [compute_alignment(A, B, loss_matrix, x_indexdict, y_indexdict) for A, B in sequences]
    write_output(alignments, outputfile)    

if __name__ == "__main__":
    main(sys.argv[1:])