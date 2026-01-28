"""For DNA strings s1 and s2 having the same length, their transition/transversion ratio
 R(s1,s2) is the ratio of the total number of transitions to the total number of transversions,
where symbol substitutions are inferred from mismatched corresponding symbols as when calculating
Hamming distance (see “Counting Point Mutations”).
Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
Return: The transition/transversion ratio R(s1,s2)."""
Sample1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
Sample2 = 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'
solution = 1.21428571429

# Manuell

length = len(Sample1)
transition = 0

for i in range(length):
    if Sample1[i] == Sample2[i]:
        continue
    elif Sample1[i] == 'G' and Sample2[i] == 'T':
        transition +=1


