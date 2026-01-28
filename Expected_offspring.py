"""
Calculate the nummber of offspring with the Dominant Marker:
Given: Six nonnegative integers, each of which does not exceed 20,000.
The integers correspond to the number of couples in a population possessing each genotype
pairing for a given factor.
In order, the six given integers represent the number of couples having the following genotypes:

a1 = AA-AA - 4
a2 = AA-Aa - 4
a3 = AA-aa - 4
a4 = Aa-Aa - 3
a5 = Aa-aa - 2
a6 = aa-aa - 0

Return: The expected number of offspring displaying the dominant phenotype in the next generation,
under the assumption that every couple has exactly two offspring.
"""

a1 = 19858 * 4
a2 = 18359 * 4
a3 = 18078 * 4
a4 = 17820 * 3
a5 = 18237 * 2
a6 = 17670 * 0

Ex = (a1+a2+a3+a4+a5+a6)/2
print(Ex)

# Alternative:

filepath = r"calc_offspring.txt"
displayDominant = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
offspring = 2

with open(filepath) as file:
    parentCounts = [int(x) for x in file.read().split()]

print(sum([offspring * x[0] * x[1] for x in zip(displayDominant, parentCounts)]))

# one liner:
print((sum([2 * x[0] * int(x[1]) for x in zip([1.0, 1.0, 1.0, 0.75, 0.5, 0.0], '1 0 0 1 0 1'.split())])))