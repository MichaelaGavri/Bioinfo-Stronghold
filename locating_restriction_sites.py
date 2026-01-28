"""
Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having length between 4 and 12.
You may return these pairs in any order.
"""
from Bio import SeqIO
# first read the fasta files
def find_reverse_palindromes(fasta_file):
    # Read the DNA sequence from the FASTA file
    record = next(SeqIO.parse(fasta_file, "fasta"))
    dna_sequence = str(record.seq)
    rp_dict = {}
    # print(dna_sequence)

    # Helper function to check if a sequence is a reverse palindrome
    def is_palindrome(subseq):
        conjoined = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        rev_complement = "".join(conjoined.get(base, base) for base in reversed(subseq))
        return subseq == rev_complement

    # Loop through positions and lengths in the DNA sequence
    for position in range(len(dna_sequence)):
        for length in range(4, 13):  # Palindromes of length 4 to 12
            if position + length > len(dna_sequence):
                break
            subseq = dna_sequence[position:position + length]
            if is_palindrome(subseq):
                rp_dict[(position + 1)] = length  # Store 1-based position and length

    for pos, length in rp_dict.items():
        print(f"{pos} {length}")
    return rp_dict

reverse_palindromes = find_reverse_palindromes('locating_restriction_sites.txt')