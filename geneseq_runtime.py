import random
import time
from gene_seq_checker import compute_alignment, read_cost_matrix

def generate_random_sequence(length):
    return ''.join(random.choice("ATGC") for _ in range(length))

def generate_sequence_pairs(length, num_pairs=10):
    pairs = []
    for _ in range(num_pairs):
        seq1 = generate_random_sequence(length)
        seq2 = generate_random_sequence(length)
        pairs.append((seq1, seq2))
    return pairs

def measure_average_runtime(lengths, num_pairs=10):
    results = {}
    costfile = 'imp2cost.txt'
    loss_matrix, x_indexdict, y_indexdict = read_cost_matrix(costfile)

    for length in lengths:
        sequence_pairs = generate_sequence_pairs(length, num_pairs)
        total_time = 0

        for seq1, seq2 in sequence_pairs:
            start_time = time.time()
            compute_alignment(seq1, seq2, loss_matrix, x_indexdict, y_indexdict)
            total_time += time.time() - start_time

        average_time = total_time / num_pairs
        results[length] = average_time

    return results

if __name__ == "__main__":
    lengths = [500, 1000, 2000, 4000, 5000]
    # lengths = [10, 20, 50, 100]
    results = measure_average_runtime(lengths)

    print("Average runtimes (in seconds):")
    for length, avg_time in results.items():
        print(f"Length: {length}, Average Time: {avg_time:.6f} seconds")
