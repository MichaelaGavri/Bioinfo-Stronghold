'''
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
'''


org = 'GTCA'
bases = list(org)
conjoined = {'A':'T','T':'A','C':'G','G':'C'}
rev_compement = "".join(conjoined.get(base, base) for base in reversed(org))
print(rev_compement)
