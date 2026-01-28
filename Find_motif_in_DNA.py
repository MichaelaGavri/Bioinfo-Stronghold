"""
Find a certain motif in the DNA and show where in the DNA it is positioned.

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
Example:
    GATATATGCATATACTT
    ATAT
Output:
    2,4,10
"""
input_file = 'find_motif.txt'

with open(input_file) as file:
    dna = file.readline().strip()
    motif = file.readline().strip()

positions = []
for i in range(len(dna)+1):
    if dna[i:i+len(motif)] == motif:
        positions.append(i+1)

print(*positions, sep=' ')

# Alternative

input_file = 'find_motif.txt'

with open(input_file) as file:
    dna1 = file.readline().strip()
    dna2 = file.readline().strip()
i = dna1.find(dna2)
while i != -1:
    print(i + 1),
    i = dna1.find(dna2, i + 1)
