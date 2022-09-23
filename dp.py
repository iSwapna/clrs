#!/usr/bin/env python3

'''
   CLRS: 14.1 Rod Cutting

Given a rod of length n inches and a table of prices p_i for i = 1, 2,...n, determine the
maximum revenue r_n obtained by cutting up the rod and selling the pieces. If the price p_n for a
rod of length n is large enough, an optimal solution might require no cutting at all.
'''

price = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17,
         7:17, 8:20, 9:24, 10:30}

def cut_rod(p, n):

    assert(n > 0)

    cost = [0]
    cuts = [0]
    
    for i in range(1, n+1):
        cost.append(p[i])
        cuts.append(i)
        
        for j in range(1, i):
            
            if p[j] + cost[i-j] > cost[i]:
                cost[i] = p[j] + cost[i-j]
                cuts[i] = j

    res = "" + str(cost[n])
    while n:
        res = res + str(cuts[n])
        n -= cuts[n]

    return res

def cut_rod_naive(p, n):

    assert(n > 0)

    cost = [0]
    cuts = []
    
    for i in range(1, n+1):
        cost.append(p[i])

        for j in range(i):
            cost[i] = max(cost[i], cost[j] + cost[i-j])

    return cost[n]

if __name__ == "__main__":

    assert(cut_rod(price, 1) == "11")
    assert(cut_rod(price, 2) == "52")
    assert(cut_rod(price, 8) == "2226")
    assert(cut_rod(price, 10) == "3010")
