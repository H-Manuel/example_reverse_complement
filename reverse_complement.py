"""
This script should provide the function "reverse_complement" that takes a DNA sequence as input and returns the reverse complement of the sequence.
"""


def reverse_complement(dna_sequence: str)->str:
    output=[]
    for i in dna_sequence:
        if (i == "A"):
            output.append("T")
        if (i == "T"):
            output.append("A")
        if (i == "G"):
            output.append("C")
        if (i == "C"):
            output.append("G")

    output.reverse()
  

    string=''.join(output)        
    return string

    # python -m unittest discover test