def read_fasta(file_path):
    sequence = ""

    with open(file_path, "r") as file:
        for line in file:
            if not line.startswith(">"):
                sequence += line.strip().upper()

    return sequence
