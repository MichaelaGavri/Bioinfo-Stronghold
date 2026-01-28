'''
Problem

Say that we have strings s=s1s2⋯sm and t=t1t2⋯tn with m<n. Consider the substring t′=t[1:m]. We have two cases:

If s=t′, then we set s<Lext because s is shorter than t (e.g., APPLE<APPLET).
Otherwise, s≠t′. We define s<Lext if s<Lext′ and define s>Lext if s>Lext′ (e.g., APPLET<LexARTS because APPL<LexARTS).

Given: A permutation of at most 12 symbols defining an ordered alphabet 𝒜 and a positive integer n (n≤4).

Return: All strings of length at most n formed from 𝒜, ordered lexicographically. (Note: As in “Enumerating k-mers
Lexicographically”, alphabet order is based on the order in which the symbols are given.)
'''
#sample input
alph = 'D S I C J W M G F N U'
n = 3
# liste aus string und !nicht alphabeitisch sortiert
#kompliziert aber funktioniert:
'''
alph_list= []
for i in alph:
    if i == ' ':
        pass
    else:
        alph_list.append(i)
'''
#eifacher mit split(definiere separator)
alph_list = alph.split()
# erstelle alle kobis bis zur länge n

############################## LÖSUNG 1 ###################################
def gen_strings(alphabet, n):
    # Base case: if length is 0, return an empty string
    if n == 0:
        return [""]

    # Recursive case: for each symbol in the alphabet, prepend it to all strings of length (n-1)
    smaller_strings = gen_strings(alphabet, n-1)
    result = []
    for symbol in alphabet:
        for s in smaller_strings:
            result.append(symbol + s)
    return result

def get_all_strings(alphabet, max_length):
    result = []
    for length in range(1, max_length + 1):  # Iterate over lengths 1 to max_length
        result.extend(gen_strings(alphabet, length))
    return result


results = get_all_strings(alph_list,n)
# sort list by given alphabet

def sort_by_custom_alphabet(strings, custom_alphabet):
    # Create a mapping of each character to its position in the custom alphabet
    custom_order = {char: index for index, char in enumerate(custom_alphabet)}

    # Define a key function for sorting
    def custom_key(string):
        return [custom_order[char] for char in string]  # Map each character to its position

    # Sort the strings using the custom key
    return sorted(strings, key=custom_key)

sorted_result = sort_by_custom_alphabet(results,alph)

file = open('Ordering_var_strings.txt', 'w')

for i in sorted_result:
    file.write(i+'\n')
file.close()

# das funktioniert aber ist sehr Lang

############################## LÖSUNG 2 ###################################

input = """
D N A
3
""".strip('\n').split('\n') #speichert input als liste mit alph(str) und n(str) als einträge

alphabet, n = input[0].split(), int(input[1]) # teilt alphabet und n in unabhängige variablen (kombo)

def generate(n, h=""): #h hat hier ein default value, heist wenn nicht h vorhanden dann ist es ein leerer str
    print(h) # anstadt die results zu speichern wird h geprinted, könnte auch in einen file geschrieben werden
    if n == 0:
        return
    for c in alphabet:
        generate(n-1, h+c)

generate(n)