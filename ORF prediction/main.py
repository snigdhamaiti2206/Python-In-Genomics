START_CODON = "ATG"
STOP_CODONS = ["TAA", "TAG", "TGA"]


def find_orfs(sequence):
    sequence = sequence.upper()

    orf_number = 1

    for i in range(len(sequence) - 2):

        codon = sequence[i:i+3]

        if codon == START_CODON:

            for j in range(i + 3, len(sequence) - 2, 3):

                stop = sequence[j:j+3]

                if stop in STOP_CODONS:

                    orf = sequence[i:j+3]

                    print(f"\nORF {orf_number}")
                    print("-" * 30)
                    print(f"Start Position : {i + 1}")
                    print(f"Stop Position  : {j + 3}")
                    print(f"Length         : {len(orf)} bp")
                    print(f"Sequence       : {orf}")

                    orf_number += 1
                    break


dna = input("Enter DNA Sequence:\n")

find_orfs(dna)
