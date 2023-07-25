import time
def bass(a,ind,buy):
    if ind == len(a):
        return 0

    if buy:
        profit = max(bass(a,ind+1,0)-a[ind],bass(a,ind+1,1))
    else:
        profit = max(bass(a,ind+1,1)+a[ind],bass(a,ind+1,0))
    return profit
def basso(a,ind,buy,dp):

    if ind == len(a):
        return 0
    if dp[ind][buy]!=-1:
        return dp[ind][buy]     
    if buy:
        profit = max(basso(a,ind+1,0,dp)-a[ind],basso(a,ind+1,1,dp))
    else:
        profit = max(basso(a,ind+1,1,dp)+a[ind],basso(a,ind+1,0,dp))
    dp[ind][buy] = profit
    
    return dp[ind][buy]
def tabulation(dp,a):
    n = len(a)
    dp[n][0]=dp[n][1]= 0

    for ind in range(n-1,-1,-1):
        for buy in range(2):
            if buy:
                profit = max(dp[ind+1][0]-a[ind],dp[ind+1][1])
            else:
                profit = max(dp[ind+1][1]+a[ind],dp[ind+1][0])
            dp[ind][buy] = profit
    
    return dp[0][1]
def optimal(a):
    dp =[0]*2
    curr = [0]*2
    n = len(a)
    dp[0]=dp[1]= 0
  
    for ind in range(n-1,-1,-1):
        
            curr[1]= max(dp[0]-a[ind],dp[1])
            curr[0]= max(dp[1]+a[ind],dp[0])
            dp = curr
    return dp[1]    
 


prices = [7,1,5,3,6,4,2,3,4,5,6,7,8,5,5]
dp = [[0 for j in range(2)] for i in range(len(prices)+1)]

# a = time.time()
# print(bass(prices,0,1))
# print(time.time()-a)
# b = time.time()
# print(basso(prices,0,1,dp))
# print(time.time()-b)
print(optimal(prices))



