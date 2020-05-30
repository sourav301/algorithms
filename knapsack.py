# -*- coding: utf-8 -*-
"""
Created on Sat May 30 20:38:32 2020

@author: SIBSANKAR
"""


val = [60, 100, 120] 
wt = [10, 20, 30] 
max_weight = 50

def knapsack_top_down(n, remaining_weight):
    if remaining_weight==0 or n==0:
        return 0
    if remaining_weight<wt[n] :
        return knapsack_top_down(n-1, remaining_weight)
    else:
        including = knapsack_top_down(n-1, remaining_weight-wt[n])+val[n]
        excluding = knapsack_top_down(n-1, remaining_weight)
        
        return max(including,excluding)
    
    
memo = [[None]*(max_weight+1)] * (len(wt) +1)
def knapsack_top_down_dp(n, remaining_weight):
    if memo[n][remaining_weight]!=None:
        return memo[n][remaining_weight]
    if remaining_weight==0 or n==0:
        return 0
    if remaining_weight<wt[n] :
        return knapsack_top_down(n-1, remaining_weight)
    else:
        including = knapsack_top_down_dp(n-1, remaining_weight-wt[n])+val[n]
        excluding = knapsack_top_down_dp(n-1, remaining_weight)
        max_value = max(including,excluding)
        memo[n][remaining_weight] = max_value
        return max_value
    

    
def knapsack_bottom_up_dp(n,max_weight):
    
    for i in range(max_weight+1):
        memo[0][i] = 0
        
    for i in range(1,n):
        for c in range(max_weight+1):
            
            include,exclude=0,0
            
            if c>=wt[i]:
                include = val[i]+memo[i-1][c-wt[i]]
            else:
                include = 0
            
            exclude = memo[i-1][c]
                
            memo[i][c]=max(include,exclude)
    
    return memo[-1][-1]
            

    


# print(knapsack_top_down_dp(2, max_weight))
print(knapsack_bottom_up_dp(3, max_weight))

