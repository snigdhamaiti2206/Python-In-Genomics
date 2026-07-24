def detect_snps(reference, sample):
    if len(reference) != len(sample):
        print("Error: DNA sequences must be the same length.")
        return

    snps = []

    for i in range(len(reference)):
        if reference[i] != sample[i]:
            snps.append((i + 1, reference[i], sample[i]))

    if len(snps) == 0:
        print("No SNPs found.")
    else:
        print(f"Total SNPs Found: {len(snps)}\n")

        print("Position\tReference\tSample")

        for snp in snps:
            print(f"{snp[0]}\t\t{snp[1]}\t\t{snp[2]}")


reference = input("Enter Reference DNA Sequence: ").upper()
sample = input("Enter Sample DNA Sequence: ").upper()

detect_snps(reference, sample)
