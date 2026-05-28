"""
Random Sequence Generator
This script generates a random DNA sequence of a specified length.
The DNA sequence is composed of the four bases: Adenine (A), Thymine (T), Cytosine (C), and Guanine (G).
The user can specify the length of the random DNA sequence by changing the value in the range function in the for loop.
In this example, it generates a random DNA sequence with 10 base pairs.
The script uses the `random` module to randomly select bases from the list of bases
and constructs the random DNA sequence by concatenating the selected bases into a string.
Finally, it prints the generated random DNA sequence.
"""

# This script generates a random DNA sequence of a specified length. The DNA sequence is composed of the four bases: Adenine (A), Thymine (T
import random

# Define the four bases of DNA
bases = ["A", "T", "C", "G"]

# Create an empty string to store the random DNA sequence
random_dna = ""

# Generate a random DNA sequence with 10 base pairs by randomly selecting bases from the list
for i in range(10):
    # randomly select a base from the list of bases and add it to the random_dna string
    random_dna += random.choice(bases)

# print the generated random DNA sequence
print(random_dna)