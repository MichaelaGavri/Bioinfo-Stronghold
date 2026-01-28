"""After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

"""
from Bio import SeqIO
from Bio.Seq import Seq

# Get file.
file = 'rosalind_splc.txt'
strings = []
for seq_record in SeqIO.parse(file, 'fasta'):
    strings.append(str(seq_record.seq))
    #print(seq_record.seq)
    #print(seq_record.id)

full_seq = strings[0]
introns = strings[1:]

# Find and delete introns
def delete_introns(seq,introns):
    for intron in introns:
        seq = seq.replace(intron, '')
    return seq

# translate exons to protein
def exon_to_protein(seq, introns):
    exon_seq = delete_introns(seq, introns)
    # Transcribe to RNA
    rna_seq = Seq(exon_seq).transcribe()
    # Translate to protein
    protein_seq = rna_seq.translate(to_stop=True)
    return str(protein_seq)

protein = exon_to_protein(full_seq, introns)
print(protein)



