"""
This script is a simple bioinformatics pipeline that reads a DNA sequence from
a FASTA file, transcribes it into RNA, and then translates the RNA into a protein sequence.
The script includes error handling to manage cases where the specified FASTA file cannot be found.
The pipeline consists of three main functions:
1. read_and_clean_fasta: Reads a FASTA file and extracts the DNA sequence,
    ensuring it is clean and free of
    whitespace
2. transcribe_dna: Transcribes a DNA string into an RNA string by replacing 'T' with 'U'.
3. translate_rna: Translates an RNA string into a protein sequence by reading codons
    (groups of 3 nucleotides) and mapping them to amino acids using a predefined codon table.
The script uses a codon table to map RNA codons to their corresponding amino acids, including stop codons. The final output is the translated protein sequence, which is printed to the console. If the specified FASTA file cannot be found, an error message is displayed to inform the user.
"""

# Dictionary mapping RNA codons to their corresponding amino acids (single-letter codes)
codon_table = {
    "AUG": "M", "UUU": "F", "GGC": "G", "CCA": "P",
    "UAA": "*", "UAG": "*", "UGA": "*"
}

# A function to read a FASTA file and extract the DNA sequence, ensuring it is clean and free of whitespace.
def read_and_clean_fasta(path):
    """ Opens the FASTA file, grabs the sequence line, and strips whitespace """

    # We open the specified FASTA file in read mode and read all lines into a list. The first line is typically a header, so we focus on the second line which contains the DNA sequence.
    with open(path, "r") as file:
        lines = file.readlines()
    
    clean_dna = lines[1].strip()
    return clean_dna

# A function to transcribe a DNA string into an RNA string by replacing 'T' with 'U'.
def transcribe_dna(dna_string):
    """Transcribes a DNA string into an RNA string."""

    # We create a translation table that maps 'T' to 'U' for the transcription process
    transcription_table = str.maketrans("T", "U")
    rna = dna_string.translate(transcription_table)
    return rna

# A function to translate an RNA string into a protein sequence by reading codons (groups of 3 nucleotides) and mapping them to amino acids.
def translate_rna(rna_string):
    """ Loops through RNA by 3s and builds a protein sequence safely """

    # Initialize an empty string to accumulate the resulting protein sequence as we translate each codon.
    protein_sequence = ""
    
    # Loop through the RNA string in steps of 3 to read codons
    for i in range(0, len(rna_string), 3):
        codon = rna_string[i:i+3]
        
        # If the codon is less than 3 nucleotides, it cannot be translated, so we break out of the loop
        if len(codon) < 3:
            break
        
        # Look up the amino acid for the codon, defaulting to "?" if the codon is not found in the table
        amino_acid = codon_table.get(codon, "?")
        
        # If the amino acid is a stop codon ("*"), we stop translating further
        if amino_acid == "*":
            break
        
        # Add the amino acid to the growing protein sequence
        protein_sequence += amino_acid

    # Return the final protein sequence after processing all codons    
    return protein_sequence

# Main execution block to read the FASTA file, transcribe the DNA, and translate it into a protein sequence.
file_path = r"C:\Users\Gebruiker\Documents\Visual Studio 18\My codes\bioinformatics\sample.fasta"

# We wrap the main processing steps in a try-except block to handle potential file-related errors gracefully.
try:
    dna_data = read_and_clean_fasta(file_path)
    rna_data = transcribe_dna(dna_data)
    final_protein = translate_rna(rna_data)
    print("Final Protein product: ", final_protein)

# If the specified file cannot be found at the given path, we catch the FileNotFoundError and print an error message to inform the user.
except FileNotFoundError:
    print("Error: The file could not be found! Please double-check your folder path.")
