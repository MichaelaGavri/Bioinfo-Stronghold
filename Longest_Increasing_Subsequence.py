"""
A subsequence of a permutation is a collection of elements of the permutation in the order that they appear.
For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease.
For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9),
and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
"""
############### Unschöne Lösung ###############
example = [8, 2, 1, 6, 5, 7, 4, 3, 9]
l_d_l=[]

def find_long(reihe,i,active_list): #liste, position, ??
    position=0
    for j in reihe:
        if j>i:
            active_list.append(j)
            rest_reihe=reihe[position:]
            find_long(rest_reihe,j,active_list)
            break
        position+=1
    return active_list

def liste_durchgehen(reihe):
    active_list=[]
    position=0
    for i in reihe:
        active_list.append(i)
        active_list.append(find_long(reihe[position:],i,active_list))
        l_d_l.append(active_list)
        active_list=[]
        position+=1


############### Lösung 2 ##############

def longest_increasing_subsequence(nums):
    if not nums:
        return []

    n = len(nums)
    dp = [1] * n  # Speichert die Länge der LIS bis zu jedem Index
    prev = [-1] * n  # Speichert die vorherigen Indizes zur Rekonstruktion der Sequenz

    max_length = 0
    max_index = 0

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

        if dp[i] > max_length:
            max_length = dp[i]
            max_index = i

    # Rekonstruiere die längste aufsteigende Sequenz
    lis = []
    while max_index != -1:
        lis.append(nums[max_index])
        max_index = prev[max_index]

    return lis[::-1]  # Umkehrung für richtige Reihenfolge


# Beispielaufruf
with open('samples/Longest_Increasing_Subsequence.txt', 'r') as file:
    lines = file.readlines()
    n = int(lines[0].strip())  # Erste Zeile gibt die Länge der Liste vor
    example = list(map(int, lines[1].split()))[:n]  # Zahlen aus zweiter Zeile

result = longest_increasing_subsequence(example)

with open('output.txt', 'w') as file:
    for i in result:
        file.write(str(i) + ' ')
        file.write('\n')

print(result)

