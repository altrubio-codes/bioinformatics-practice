"""
This code reads a FASTA file, extracts the header and sequence,
and prints them to the console.
The FASTA format typically consists of a header line that starts with '>'
followed by the sequence data on the next line(s). In this example,
we assume that the FASTA file contains only one sequence for simplicity.
The code uses the `open` function to read the file,
and the `readlines` method to get all lines as a list.
It then uses the `strip` methodto remove any leading or trailing whitespace from the header
and sequence lines before printing them.
"""

# Open the file in 'r' (read) mode
file_path = r"c:\Users\Gebruiker\Documents\Visual Studio 18\My codes\bioinformatics\sample.fasta"

# Pass the file_path variable here instead of the raw text string
with open(file_path, "r") as file:
    # Read all lines from the file into a list
    lines = file.readlines()

# Print the lines to see how Python reads them
print(lines)

# Remove any leading/trailing whitespace from the first line to get the header
header = lines[0].strip()

# Remove any leading/trailing whitespace from the second line to get the sequence
sequence = lines[1].strip()

# Print the header and sequence to verify they were read correctly
print("Header:", header)
print("Sequence:", sequence)