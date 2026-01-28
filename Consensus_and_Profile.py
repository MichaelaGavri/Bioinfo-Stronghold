"""
###### Unsolved
Create an array listing the amount of each aminoacid in each position of multiple dna fragments.
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection.
(If several possible consensus strings exist, then you may return any one of them.)
"""
from Bio import SeqIO
# Get file.
file = 'rosalind_cons.txt'
strings = []
for seq_record in SeqIO.parse(file, 'fasta'):
    strings.append(str(seq_record.seq))
    # print(seq_record.seq)
    # print(seq_record.id)
    # print(len(seq_record))
# print(strings[0])
# print(strings[1])

# make a profile matrix

n = len(strings[0])
profile_matrix = {
    'A': n*[0],
    'C': n*[0],
    'G': n*[0],
    'T': n*[0]
}

for i in strings:
    for position, nucleotide in enumerate(i):
        profile_matrix[nucleotide][position] +=1

# get consensus profile
consensous = []

for position in range(len(profile_matrix['A'])):
    max_count = 0
    max_nucleotide = None
    for nucleotide in ['A','C','G','T']:
        count = profile_matrix[nucleotide][position]
        if count > max_count:
            max_count = count
            max_nucleotide =nucleotide
    consensous.append(max_nucleotide)
consensous = ''.join(consensous)
print(consensous)
