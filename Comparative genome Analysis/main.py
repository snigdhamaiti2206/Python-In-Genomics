import pandas as pd

def read_fasta(file_path):
    sequence = ""

    with open(file_path, "r") as file:
        for line in file:

            # Ignore FASTA header
            if not line.startswith(">"):
                sequence += line.strip().upper()

    return sequence

# Calculate genome length
def genome_length(sequence):
    return len(sequence)

# Calculate GC content
def gc_content(sequence):
    gc = sequence.count("G") + sequence.count("C")

    return round((gc / len(sequence)) * 100, 2)

# Count nucleotides
def nucleotide_count(sequence):
    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }

# Compare genomes
def compare(files):

    results = []

    for bacteria, file in files.items():

        sequence = read_fasta(file)

        counts = nucleotide_count(sequence)

        results.append({
            "Bacteria": bacteria,
            "Genome Length": genome_length(sequence),
            "GC %": gc_content(sequence),
            "A": counts["A"],
            "T": counts["T"],
            "G": counts["G"],
            "C": counts["C"]
        })

    return pd.DataFrame(results)

files = {
    "E_coli": r"C:\Github Files\ecoli.fasta",
    "Bacillus": r"C:\Github Files\bacillus.fasta",
    "Salmonella": r"C:\Github Files\salmonella.fasta"
}

# Perform comparative analysis
df = compare(files)

# Print results
print("\n========== COMPARATIVE GENOME ANALYSIS ==========\n")

print(df)

# Save results
df.to_csv(
    r"C:\Github Files\genome_comparison.csv",
    index=False
)


print("\nResults saved successfully!")
