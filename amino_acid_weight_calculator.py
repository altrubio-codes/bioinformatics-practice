"""
Calculate the total weight of a protein sequence based on the weights of its amino acids.
The weights of the amino acids are given in the `aa_weights` dictionary.
The protein sequence is stored in the `protein` variable.
The total weight is calculated by iterating through each amino acid in the protein sequence,
looking up its weight in the `aa_weights` dictionary,
and summing these weights to get the total weight of the protein.
"""

# Define the weights of the amino acids in a dictionary
aa_weights = {
    "A" : 89.1,
    "G" : 75.1,
    "V" : 117.1
}

# Define the protein sequence
protein = "AGVGA"

# Initialize the total weight to zero
total_weight = 0.0

# Look into each index of protein sequence, each letter found store it in aa, then look up the weight of that amino acid in the aa_weights dictionary and add it to the total weight
for aa in protein:
    total_weight += aa_weights[aa]

# Print the total weight of the protein
print(total_weight)