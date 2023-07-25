def recursion(a,ind,buy,cap):
    if cap == 0:
        return 0
    if ind == len(a):
        return 0

    if buy:
        profit = max(memo(a,ind+1,0,cap)-a[ind],memo(a,ind+1,1,cap))
    else:
        profit = max(memo(a,ind+1,1,cap-1)+a[ind],memo(a,ind+1,0,cap))
    return profit  
def memo(a,ind,buy,cap,dp):
    if cap == 0:
        return 0
    if ind == len(a):
        return 0
    if dp[ind][buy][cap]!=-1:
        return dp[ind][buy][cap]
    if buy:
        dp[ind][buy][cap] = max(memo(a,ind+1,0,cap,dp)-a[ind],memo(a,ind+1,1,cap,dp))
    else:
        dp[ind][buy][cap]= max(memo(a,ind+1,1,cap-1,dp)+a[ind],memo(a,ind+1,0,cap,dp))
    return dp[ind][buy][cap]
def tabulation(dp,ind,buy,cap,a):
    n=len(a)
    for ind in range(n-1,-1,-1):
        for buy in range(2):
            for cap in range (1,3):
                if buy:
                    profit = max(dp[ind+1][0][cap]-a[ind],dp[ind+1][1][cap])
                else:
                    profit= max(dp[ind+1][1][cap-1]+a[ind],dp[ind+1][0][cap])
                dp[ind][buy][cap]=profit

    return dp[0][1][2]

def optimal(a):
    n=len(a)
    after = [[0 for _ in range(3)] for _ in range(2)]
    cur = [[0 for _ in range(3)] for _ in range(2)]
    for ind in range(n-1,-1,-1):
        for buy in range(2):
            for cap in range (1,3):
                if buy:
                    cur[buy][cap] = max(after[0][cap]-a[ind],after[1][cap])
                else:
                    cur[buy][cap] = max(after[1][cap-1]+a[ind],after[0][cap])
        after = cur
    return after[1][2]    


        

prices = [3,3,5,0,0,3,1,4]
t = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(len(prices)+1)]
# print(memo(prices,0,1,2,t))
# print(tabulation(t,0,1,2,prices))
print(optimal(prices))

