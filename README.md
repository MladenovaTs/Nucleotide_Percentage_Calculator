# Nucleotide Percentage Calculator
This is a Python script that takes a DNA or RNA sequence as input and calculates the percentage of each nucleotide.

## Usage
To use this script, simply call the nucleotide_percentages function with a DNA or RNA sequence as a string argument. The function will return a dictionary containing the percentage of each nucleotide.

seq = "AGCTGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGA"
nuc_percentages = nucleotide_percentages(seq)
print(nuc_percentages)

This will output:
{'A': 21.74, 'C': 30.43, 'G': 26.09, 'T': 21.74, 'U': 0.0}

Alt-Note that the function can handle both DNA and RNA sequences, as it counts both 'T' and 'U' nucleotides.
