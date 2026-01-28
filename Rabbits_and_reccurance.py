"""
Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each
generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

Wiederholung:
F1 = F2 = 1
Fn = Fn-1 + Fn-2

In diesem fall aber:
F1 = F2 = 1
Fn = 3*Fn-1 + Fn-2
"""


def Fibonaci(n, multiplier):
    multiplier = multiplier
    if n in {0, 1, 2}:
        return 1
    return Fibonaci(n-1, multiplier)+Fibonaci(n-2, multiplier)*multiplier


# Mortal Rabbits

'''
In diesem Fall streben die Rabbits nach m Monaten

F1 = F2 = 1
Fn = Fn-1 + Fn-2 - Fn-m
'''


def mortal_rabbits(n, m):
    bunnies = [1, 1]
    months = 2
    count = []
    while months < n:
        if months < m:
            bunnies.append(bunnies[-2]+bunnies[-1]) # positionen vin hintern!
            print('1 debug:',m , bunnies)
        elif months == m or count == m+1:
            bunnies.append(bunnies[-2]+bunnies[-1]-1)
            print('2 debug:',m,  bunnies)
        else:
            bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(m + 1)])
            print('3 debug:',m , bunnies)
        months += 1
    print(bunnies[-1])


if __name__ == "__main__":
    # print(Fibonaci(36, 3))
    print(mortal_rabbits(20, 3))
