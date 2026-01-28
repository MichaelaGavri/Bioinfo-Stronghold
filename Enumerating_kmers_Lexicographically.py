"""
Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).
"""

alph = "A B C D"
n = 4

# erstelle eine liste mit allen Buchstaben im Alpahabet

alph_list= []
for i in alph:
    if i == ' ':
        pass
    else:
        alph_list.append(i)

alph_list.sort()
# definiere perutationen

def generate_lexicographic_strings(alphabet, n):
    # Base case: if length is 0, return an empty string
    if n == 0:
        return [""]

    # Recursive case: for each symbol in the alphabet, prepend it to all strings of length (n-1)
    smaller_strings = generate_lexicographic_strings(alphabet, n - 1)
    result = []
    for symbol in alphabet:
        for s in smaller_strings:
            result.append(symbol + s)
    return result


# Example usage

result = generate_lexicographic_strings(alph_list, n)

# Print the results
for string in result:
    print(string)

# sortiere die Permutaionen der richtigen läne





