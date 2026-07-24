from compare_genomes import compare

files = {
    "E_coli": "../data/ecoli.fasta",
    "Bacillus": "../data/bacillus.fasta",
    "Salmonella": "../data/salmonella.fasta"
}

df = compare(files)

print(df)

df.to_csv("../results/genome_comparison.csv", index=False)
