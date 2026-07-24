def calculate_gc_content(sequence):
    """
    Calculate GC content of a DNA sequence.

    Parameters:
        sequence (str): DNA sequence

    Returns:
        float: GC percentage
    """

    sequence = sequence.upper().replace("\n", "").replace(" ", "")

    if len(sequence) == 0:
        return 0

    gc_count = sequence.count("G") + sequence.count("C")

    gc_percentage = (gc_count / len(sequence)) * 100

    return gc_percentage


def main():

    with open("sample_sequence.txt", "r") as file:
        dna = file.read()

    gc = calculate_gc_content(dna)

    print("=" * 35)
    print("GC Content Calculator")
    print("=" * 35)
    print(f"Sequence Length : {len(dna)} bp")
    print(f"GC Content      : {gc:.2f}%")
    print("=" * 35)


if __name__ == "__main__":
    main()
