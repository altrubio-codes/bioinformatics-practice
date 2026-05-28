"""
This script defines a hydrophobicity scale for amino acids
and uses it to determine whether each amino acid in a given protein sequence
is likely to be found inside or outside of a protein structure.
The results are printed to the console.
"""

# Dictionary defining each letter representing an amino acid and whether it is hydrophobic (inside) or hydrophilic (outside)
hydro_scale = {
    "A" : "Inside",
    "V" : "Inside",
    "R" : "Outside",
    "K" : "Outside"
}

# A variable storing the protein sequence to be analyzed
protein_sequence = "AVRKVA"

# Look into each index of protein sequence, each letter found store it in i
for i in protein_sequence:
    # Look up the stored letter in i then check hydro_scale dictionary to find if it is inside or outside and print the result
    print(hydro_scale[i])