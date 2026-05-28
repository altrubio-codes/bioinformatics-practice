"""
Motif Finder
This script identifies all occurrences of a specified motif in a given genome sequence.
It uses the `find` method to locate the motif and iterates through the genome until all occurrences are found,
printing their positions.
"""

# Define the genome sequence to search through
genome = "ATGCCCCATGTTTTATG"

# Define the motif to search for
motif = "ATG"

# Find the first occurrence of the motif in the genome
position = genome.find(motif)

# Find the next occurrence of the motif starting from the position just after the first found motif
next_position = genome.find(motif, position +1)

# Start searching for the motif from the beginning of the genome
current_pos = genome.find(motif)

# Print the positions of all occurrences of the motif in the genome
print("Motif found at positions:")
# Keep looping as long as a match is found (not -1)
while current_pos != -1:
    print(current_pos)
    # Search again, starting just after the match we just found
    current_pos = genome.find(motif, current_pos + 1)