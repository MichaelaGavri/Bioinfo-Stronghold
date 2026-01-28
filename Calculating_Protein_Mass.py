# get monoistopic table

f = open('monoistopic_mass_table.txt', 'r')
mass_table = {}
for i in f.readlines():
    j = i.split()
    for k in j:
        mass_table[j[0]] = float(j[1])

# get protein sequence

protein = open('prot_string.txt', 'r')
protein = protein.read()
protein = protein.strip()

# get protein mass

protein_mass = 0
for i in protein:
    protein_mass += mass_table[i]
print(protein_mass)

# alternative

print("%.2f" % sum(map(lambda x: mass_table[x], protein)))
# "%.2f"% besagt dass auf zweite nachkommestelle aufgerundet sein soll

# andere alternative

print("%.2f" % sum([mass_table[i] for i in protein]))
