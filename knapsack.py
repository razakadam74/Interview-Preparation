
'''
Recursive
Time complexity : 0(2 ^n)
Space Complexity : 0(1)
'''
def knapsack(weight, values, weights, n):
    if weight == 0 or n ==0 :   
        return 0
    
    if weights[n-1] > weight:
        return knapsack(weight,values,weights, n-1)
    else:
        return max(values[n-1] + knapsack(weight - weights[n-1], values, weights,n-1), knapsack(weight, values, weights, n-1));


def knapsackDynamic(weight, values, weights, n):
    K = [[0] * (weight +1)] * (n+1)
    print(len(K))
    for i in range(n + 1):
        for w in range(weight + 1):
            if i ==0 or w == 0:
                K[i][w] = 0
            elif weights[i -1] <= weight:
                K[i][w] = max(values[i -1] + K[i-1][w - weights[i -1]], K[i -1][w])
            else:
                K[i][w] = K[i-1][w]
    # print(K)
    return K[n][weight]


# W = 70
# values = [60,100,120,125,130,140]
# weights = [10,20,30,35,40,44]
# #result = knapsack(W, values, weights, 6)
# result = knapsackDynamic(W, values, weights, 6)
# print(result)
