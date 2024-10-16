# distance hamming in Python
"""
    Error detection and correction, Bioinformatics, Network routing,
    Cryptography, Biodiversity, Genetics, and Ecology
"""

def hamming(string1, string2):
    """
    Function to calculate the Hamming distance between two strings
    """
    if len(string1) != len(string2):
        raise ValueError("The strings must have the same length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(string1, string2))

print(hamming("arlan", "allan"))  # 3