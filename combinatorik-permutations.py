# permuatationen sind alle möglichen kombinationen von Zahlen innerhalb eines bereiches n
n = 6 # definiere die Länge der Permutation
# zuerst die Anzahl der Permutationen berechnen - die Fakultät der lenge n - n!
# nur mit build in
fak_n = 1
for i in range(1, n+1): fak_n *= i
# sonnst auch möglich über mathe
# oder mit rekursion:


def fakultaet(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * fakultaet(n-1)

# nun finde alle kombinationen
# zuerst ertelle Liste der Zahlen:

lst = list(range(1,n+1))
# nun definiere permutationen:


def permutation(liste):
    if len(liste) == 0:
        return [[]]
    results = []

    for i in range(len(liste)):
        current = liste[i]
        remaining = liste[:i] + liste[i+1:]
        for perm in permutation(remaining):
            results.append([current] + perm)
    return results

with open('output.txt', 'w') as file:
    file.write(str(fakultaet(n)) + '\n')
    for i in (permutation(lst)):
        string_representation = ' '.join(map(str, i)) # um Ergebniss als string mit leerzeichen darzustellen.
        file.write(string_representation + '\n')
