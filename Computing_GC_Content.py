"""
Calculate the relative content of cg in a DNA string that is labeled by ">Rosalind_xxxx"
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated;
please see the note on absolute error below.

Pseudocode:
def calculate the cg content (of string)
    samle dict = empty
    for i in string:
        if i = >:


"""

text = open('rosalind_gc.txt', 'r')
cg_dict = {}
f = text.readlines()
for i, line in enumerate(f):
    if line.startswith('>'):
        sample_name = line[1:]
        sample_name = sample_name.strip()
        seq = ''
    else:
        new_seq = line.strip()
        seq = seq + new_seq
        if i == len(f) - 1 or f[i + 1].startswith('>'):
            gc = 100 * (seq.count('G') + seq.count('C')) / len(seq)
            cg_dict[sample_name] = gc   # to store all gc content, to only store max do following
            # if gc > max_gc:
            # max_gc = gc
            # max_id = id
# find max
maximum = max(cg_dict, key=cg_dict.get)
print(cg_dict)
print(maximum, cg_dict[maximum])
