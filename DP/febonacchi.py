def feb(n,dp):
    if n<=1:
        return n
    if dp[n] != -1:
        return dp[n]
    a = dp[n]= feb(n-1,dp) + feb(n-2,dp) 
    # print(a)   
    return a
def optimal(n):
    prev2 = 0
    prev =1  
    for i in range(2,n+1):
        curr = prev2 +prev
        prev2 = prev
        prev = curr
    return prev    

a =5
dp = [-1]*6
print(feb(a,dp),'\t',optimal(50))