#written in Python 3.0

def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return get_length(dna1) > get_length(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    occurence = 0
    
    for letter in dna:
        if letter == nucleotide:
            occurence = occurence + 1

    return occurence

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool
    
    Returns True if and only if DNA sequence dna does not contain characters other than 'A', 'C', 'T' or 'G'
    
    >>> is_valid_sequence('ATCGC')
    True
    >>> is_valid_sequence('atCC')
    False
    >>> is_valid_sequence('ABCDE')
    False
    """
    valid = 'ACTG'
    match = 0
    
    for letter in dna:
        if letter in valid:
            match = match + 1

    return match == len(dna)

def insert_sequence(dna1,dna2,p):
    """ (str, str, int) -> str

    Returns the DNA str that results from dna2 being inserted into dna1 at position p

    >>> insert_sequence('CCGG','AT',2)
    CCATGG
    >>> insert_sequence('CCGG','AT',0)
    ATCCGG
    >>> insert_sequence('CCGG','AT',10)
    CCGGAT
    """
    return dna1[:p]+ dna2 + dna1[p:]
    
def get_complement(nucleotide):
    """ (str) -> str

    Return the str complement of the nucleotide

    >>>get_complement('A')
    T
    >>>get_complement('T')
    A
    >>>get_complement('C')
    G
    >>>get_complement('G')
    C
    """
    
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
        
def get_complementary_sequence(dna):
    """ (str) -> str

    Return the str complement of the dna

    >>>get_complementary_sequence('ATCG')
    TAGC
    """
    
    ini = ''
    for letter in dna:
        ini = ini + get_complement(letter)

    return ini
