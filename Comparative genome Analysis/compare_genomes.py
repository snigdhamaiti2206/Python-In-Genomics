import pandas as pd

from fasta_reader import read_fasta
from genome_stats import genome_length
from genome_stats import gc_content
from genome_stats import nucleotide_count


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

    df = pd.DataFrame(results)

    return df
