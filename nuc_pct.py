
#!/usr/bin/env python

"""
Python script that takes a DNA or RNA sequence as input and computes the percentage of each nucleotide
"""

def nucleotide_percentages(seq):
    """
    This function takes a DNA or RNA sequence as input and returns the percentage of each nucleotide.
    """
    seq = seq.upper()  # convert the sequence to uppercase to make it case-insensitive
    nuc_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0, 'U': 0}  # initialize a dictionary to count the nucleotides
    
    for nuc in seq:
        if nuc in nuc_counts:
            nuc_counts[nuc] += 1  # increment the count for the corresponding nucleotide
    
    seq_len = len(seq)
    nuc_pct = {nuc: round((count / seq_len) * 100, 2) for nuc, count in nuc_counts.items()}  # compute the percentages
    

    return nuc_pct
    print (nuc_pct)

