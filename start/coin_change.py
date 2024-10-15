# greedy algorithm in Python

coins = [100, 50, 5, 1]
sol = []
sum_change = 0
change = 113

i = 0 

while i < len(coins) and sum_change != change:
    
    if sum_change + coins[i] <= change:
        sum_change += coins[i]
        sol.append(coins[i])
    else:
        i += 1

print(sol) 