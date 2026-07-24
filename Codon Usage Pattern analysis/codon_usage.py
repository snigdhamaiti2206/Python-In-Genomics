from collections import Counter

def read_sequence(file_path):
    with open(file_path, "r") as file:
        sequence = file.read().strip().upper()

    sequence = sequence.replace("\n", "")
    return sequence


def count_codons(sequence):
    codons = []

    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]

        if len(codon) == 3:
            codons.append(codon)

    return Counter(codons)


def print_results(counter):
    total = sum(counter.values())

    print(f"\nTotal Codons: {total}\n")

    print("{:<8} {:<10} {:<10}".format("Codon", "Count", "Frequency"))

    print("-" * 30)

    for codon, count in sorted(counter.items()):
        frequency = count / total
        print("{:<8} {:<10} {:.4f}".format(codon, count, frequency))


if __name__ == "__main__":

    sequence = read_sequence("sample_sequence.txt")

    codon_counter = count_codons(sequence)

    print_results(codon_counter)
