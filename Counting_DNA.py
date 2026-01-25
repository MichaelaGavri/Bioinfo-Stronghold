'''
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the
symbols 'A', 'C', 'G', and 'T' occur in s.
'''
f = open("counting_dna.txt")
DNA = f.read().rstrip()
f.close()

alphabet = {}
for letter in DNA:
    if letter not in alphabet:
        alphabet[letter] = 1
    else:
        alphabet[letter] += 1

print(alphabet['A'], alphabet['C'], alphabet['G'], alphabet['T'])

### Alternative ###

def qt(DNA):
    return print( DNA.count("A"), DNA.count("G"), DNA.count("C"), DNA.count("T"))

if __name__ == "__main__":
    qt(DNA)