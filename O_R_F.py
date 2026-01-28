# Given a DNA sequence, conjure all possible reading frames for the DNA and its reverse complememnt

def make_reverse_complement(dna):
    reverse_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_dna = ''
    for acid in reversed(dna):  # nicht vergessen DNA umzudrehen
        if acid not in reverse_dict:
            raise ValueError(f'this acid is not defined in dict: {acid}')
        reverse_dna += reverse_dict[acid]
    return reverse_dna

# make every posible string for different translation starting positions
# do not transcibe to RNA, because DNA codons can be used more efficiently


def every_translation(dna, reverse_dna):
    list_of_strings = []
    for frame in range(3):
        list_of_strings.append(dna[frame:])
        list_of_strings.append(reverse_dna[frame:])
    return list_of_strings

# print(every_translation(DNA_string,make_reverse_complement(DNA_string)))
# now search for all open reading frames (everything between the start and stop codon


def all_open_reading_frames(dna):
    dna_list = every_translation(dna, make_reverse_complement(dna))
    stop_codons = {'TAA', 'TAG', 'TGA'}
    candidate_protein_strings = []

    for string in dna_list:
        length = len(string)
        i = 0
        while i < length:
            if string[i:i+3] == 'ATG':
                for j in range(i+3, length, 3):
                    if string[j:j+3] in stop_codons:
                        candidate = string[i:j+3]
                        candidate_protein_strings.append(candidate)
                        break
            i += 3
    return candidate_protein_strings


def translate_orfs(dna):
    codon_dict = {
        'TCA': 'S',  # Serina
        'TCC': 'S',  # Serina
        'TCG': 'S',  # Serina
        'TCT': 'S',  # Serina
        'TTC': 'F',  # Fenilalanina
        'TTT': 'F',  # Fenilalanina
        'TTA': 'L',  # Leucina
        'TTG': 'L',  # Leucina
        'TAC': 'Y',  # Tirosina
        'TAT': 'Y',  # Tirosina
        'TAA': '*',  # Stop
        'TAG': '*',  # Stop
        'TGC': 'C',  # Cisteina
        'TGT': 'C',  # Cisteina
        'TGA': '*',  # Stop
        'TGG': 'W',  # Triptofano
        'CTA': 'L',  # Leucina
        'CTC': 'L',  # Leucina
        'CTG': 'L',  # Leucina
        'CTT': 'L',  # Leucina
        'CCA': 'P',  # Prolina
        'CCC': 'P',  # Prolina
        'CCG': 'P',  # Prolina
        'CCT': 'P',  # Prolina
        'CAC': 'H',  # Histidina
        'CAT': 'H',  # Histidina
        'CAA': 'Q',  # Glutamina
        'CAG': 'Q',  # Glutamina
        'CGA': 'R',  # Arginina
        'CGC': 'R',  # Arginina
        'CGG': 'R',  # Arginina
        'CGT': 'R',  # Arginina
        'ATA': 'I',  # Isoleucina
        'ATC': 'I',  # Isoleucina
        'ATT': 'I',  # Isoleucina
        'ATG': 'M',  # Methionina ######
        'ACA': 'T',  # Treonina
        'ACC': 'T',  # Treonina
        'ACG': 'T',  # Treonina
        'ACT': 'T',  # Treonina
        'AAC': 'N',  # Asparagina
        'AAT': 'N',  # Asparagina
        'AAA': 'K',  # Lisina
        'AAG': 'K',  # Lisina
        'AGC': 'S',  # Serina
        'AGT': 'S',  # Serina
        'AGA': 'R',  # Arginina
        'AGG': 'R',  # Arginina
        'GTA': 'V',  # Valina
        'GTC': 'V',  # Valina
        'GTG': 'V',  # Valina
        'GTT': 'V',  # Valina
        'GCA': 'A',  # Alanina
        'GCC': 'A',  # Alanina
        'GCG': 'A',  # Alanina
        'GCT': 'A',  # Alanina
        'GAC': 'D',  # Acido Aspartico
        'GAT': 'D',  # Acido Aspartico
        'GAA': 'E',  # Acido Glutamico
        'GAG': 'E',  # Acido Glutamico
        'GGA': 'G',  # Glicina
        'GGC': 'G',  # Glicina
        'GGG': 'G',  # Glicina
        'GGT': 'G'  # Glicina
    }
    orfs = all_open_reading_frames(dna)
    proteins = []
    for orf in orfs:
        decoded = ''
        for i in range(0, len(orf) - 3, 3):
            decoded += codon_dict[orf[i:i + 3]]
        proteins.append(decoded)
    proteins = set(proteins)  # um nur eine kopie zu haben
    return proteins


def read_fasta_as_string(file_path):
    with open(file_path, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

        # Ignore the header line and concatenate the rest
        sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))

    return sequence


dna_string = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
path = 'ORF_String.txt'
orf_string = (read_fasta_as_string(path))
all_protein_motifs = (translate_orfs(orf_string))

for motif in all_protein_motifs:
    print(motif)
