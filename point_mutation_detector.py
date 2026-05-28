"""
Point Mutation Detector
This script calculates the Hamming distance between two DNA strands,
which is the number of positions at which the corresponding symbols are different.
"""

# Two DNA strands are given. The task is to find the Hamming distance between them, which is the number of positions at which the corresponding symbols are different.
strand1 = "GAGCCTACTAACGGGAT"
strand2 = "CATCGTAATGACGGCCT"

# Variable to hold the number of point mutations (Hamming distance)
mutations = 0

# Go over each index of each strand and determine if the nucleotides at that position are different. If they are, increase the mutation count by 1.
for i in range(len(strand1)):
    if strand1[i] != strand2[i]:
        mutations += 1

# Print the Hamming distance
print(mutations)