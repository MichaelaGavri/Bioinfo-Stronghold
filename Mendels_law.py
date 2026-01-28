"""Given: Three positive integers k, m and n, representing a population containing k+m+n organisms:
k idividuals are homozygous dominant
m are heterozygous,
n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual
possessing a dominant allele (and thus displaying the dominant phenotype).
Assume that any two organisms can mate.

Example:
2 2 2
Output: 0,78333
"""


k = 5  # homozygot dominant
m = 10  # heterozygot
n = 20  # homozygot rezessiv
z = k + m + n

# w_x steht für wahrschinlichkeit mit welcher x Prozent einen Dominanten marker tragen werden.

w_0 = n/z * (n-1)/(z-1)  # nur homozygot rezessive paarungen bringen keine Dominanten Merkmale hervor
w_50 = n/z * m/(z-1) + m/z * n/(z-1)  # homozygot rez mit heterozygot bringt mit 50% Wahrschinlichkeit Merkmale hervor
w_75 = m/z * (m-1)/(z-1)  # nur heterozygote zusammen können eine 75% Wahrschilichkeit auf Merkmale haben

w_rezessiv = w_0 + w_75 * 0.25 + w_50 * 0.5
w_dominant = 1 - w_rezessiv
print(w_dominant)
