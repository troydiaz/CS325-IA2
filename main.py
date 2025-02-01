import numpy as np
import sys

def read_cost_matrix():
    # Reads Cost File
    with open("imp2cost.txt", 'r') as file:
        lines = file.readlines()
        
    headers = lines[0].split()
    matrix = {}
    
    for line in lines[1:]:
        values = line.split()
        row_char = values[0]
        matrix[row_char] = {headers[i]: int(values[i]) for i in range(1, len(values))}
    
    #Adding gap penalties for insertions and/or deletions
    matrix['-'] = {char: 1 for char in headers}
    for char in headers:
        matrix[char]['-'] = 1
    
    return matrix

def read_sequences():
    # Reads Input Fie
    with open("imp2input.txt", 'r') as file:
        return [line.strip().split(',') for line in file]
    
def compute_alignment(seq1, seq2, cost_matrix):
    # Computes Optimal Alignment
    m, n = len(seq1), len(seq2)
    dp = np.zeros((m + 1, n + 1), dtype=int)
    
    # Initializing DP (Dynamic Programming) Table
    for i in range(m + 1):
        dp[i][0] = dp[i - 1][0] + cost_matrix[seq1[i - 1]]['-']
    for j in range(n + 1):
        dp[0][j] = dp[0][j - 1] + cost_matrix['-'][seq2[j - 1]]
    
    # Filling DP Table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = dp[i-1][j-1] + cost_matrix[seq1[i-1]][seq2[j-1]]
            delete = dp[i-1][j] + cost_matrix[seq1[i-1]]['-']
            insert = dp[i][j-1] + cost_matrix['-'][seq2[j-1]]
            dp[i][j] = min(match, delete, insert)
            
    # Count from start to get Alignment
    aligned_seq1, aligned_seq2 = [], []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp[i][j] == dp[i-1][j-1] + cost_matrix[seq1[i-1]][seq2[j-1]]:
            aligned_seq1.append(seq1[i-1])
            aligned_seq2.append(seq2[j-1])
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i-1][j] + cost_matrix[seq1[i-1]]['-']:
            aligned_seq1.append(seq1[i-1])
            aligned_seq2.append('-')
            i -= 1
        else:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j-1])
            j -= 1
            
    return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2)), dp[m][n]

def write_output(alignments):
    # Writes alignment result to imp3output.txt (we can change the naming later)
    with open("imp3output.txt", 'w') as file:
        for seq1, seq2, cost in alignments:
            file.write(f"{seq1},{seq2}:{cost}\n")
            
def main():
    cost_matrix = read_cost_matrix()
    sequences = read_sequences()
    alignments = [compute_alignment(seq1, seq2, cost_matrix) for seq1, seq2 in sequences]
    write_output(alignments)
    
if __name__ == "__main__":
    main()
