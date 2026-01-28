# print(protein)
# try to make list with all amonoacids of the protein
'''trial_list_acids = []
for i in protein:
    trial_list_acids.append(i)
print (trial_list_acids)
'''

def peptide_combi_count(peptide):
    #first create dict for all aminoacids
    codon_count = {
        'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2,
        'G': 4, 'H': 2, 'I': 3, 'K': 2, 'L': 6,
        'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6,
        'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2,
        '*': 3  } # Stop codon
    combi = 1
    modulo = 1_000_000

    for acid in peptide:
        #print(acid)
        if acid not in codon_count:
            raise ValueError(f'not in codon {acid}')
        combi = (combi*codon_count[acid]) % modulo

    combi = (combi*codon_count['*'])%modulo
    return combi

#open file
path = 'that.txt'
with open(path,'r') as file:
    protein = file.read().strip()

#protein ='MA'
print(peptide_combi_count(protein))
