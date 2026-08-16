from collections import Counter

def read_sequence(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    sequence = ""

    for line in lines:
        line = line.strip()

        if line.startswith(">"):
            continue

        sequence += line

    sequence = sequence.upper()

    return sequence

def count_codons(sequence):
    codons = []

    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]

        if all(base in "ATGC" for base in codon):
            codons.append(codon)

    return Counter(codons)

def print_results(counter):
    total = sum(counter.values())

    print("\n========== CODON USAGE ANALYSIS ==========")
    print(f"\nTotal Codons: {total}\n")

    print("{:<8} {:<10} {:<12}".format(
        "Codon", "Count", "Frequency"
    ))

    print("-" * 32)

    for codon, count in sorted(counter.items()):
        frequency = count / total

        print("{:<8} {:<10} {:.4f}".format(
            codon, count, frequency
        ))

if __name__ == "__main__":

    file_path = r"C:\Github Files\sample_sequence.txt"

    sequence = read_sequence(file_path)

    print("Sequence successfully loaded!")
    print("Sequence length:", len(sequence), "bases")

    codon_counter = count_codons(sequence)

    print_results(codon_counter)
