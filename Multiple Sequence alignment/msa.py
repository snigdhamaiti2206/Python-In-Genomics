def read_sequences(filename):
    sequences = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip().upper()

            if line:
                sequences.append(line)

    return sequences


def align_sequences(sequences):
    max_length = max(len(seq) for seq in sequences)

    aligned = []

    for seq in sequences:
        aligned.append(seq.ljust(max_length, "-"))

    return aligned


def sequence_identity(reference, sequence):
    matches = 0

    for a, b in zip(reference, sequence):
        if a == b:
            matches += 1

    return (matches / len(reference)) * 100


def main():

    sequences = read_sequences("sequences.txt")

    aligned = align_sequences(sequences)

    print("\nAligned Sequences\n")

    for seq in aligned:
        print(seq)

    print("\nSequence Identity\n")

    reference = aligned[0]

    for i, seq in enumerate(aligned):
        identity = sequence_identity(reference, seq)
        print(f"Sequence {i+1}: {identity:.2f}%")

if __name__ == "__main__":
    main()
