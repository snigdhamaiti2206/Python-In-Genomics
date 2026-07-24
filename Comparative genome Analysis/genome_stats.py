def genome_length(sequence):
    return len(sequence)


def gc_content(sequence):
    gc = sequence.count("G") + sequence.count("C")
    return round((gc / len(sequence)) * 100, 2)


def nucleotide_count(sequence):
    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C"),
    }
