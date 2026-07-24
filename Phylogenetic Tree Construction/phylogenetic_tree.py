from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import AlignIO

alignment = AlignIO.read("sample_sequences.fasta", "fasta")

calculator = DistanceCalculator("identity")
distance_matrix = calculator.get_distance(alignment)

print("Distance Matrix:")
print(distance_matrix)

constructor = DistanceTreeConstructor()
tree = constructor.upgma(distance_matrix)

print("\nPhylogenetic Tree:")
Phylo.draw_ascii(tree)

Phylo.write(tree, "phylogenetic_tree.nwk", "newick")
print("\nTree saved as phylogenetic_tree.nwk")
