# brute force 
def sliding_window(nums,k):
    n = len(nums)
    max_values = []

    for i in range(n - k + 1):
        max_val = max(nums[i:i + k])
        max_values.append(max_val)

    return max_values
#optimal
def sliding_window_optimal(nums,k):
    dequeue = []
    ans = []
    n = len(nums)
    for i in range(n):
        if dequeue and dequeue[0] == (i -k ):
            dequeue.pop(0)
        while dequeue and nums[dequeue[-1]] < nums[i]:
            dequeue.pop(-1)  
        dequeue.append(i)
        if  i >= k-1:
            ans.append(nums[dequeue[0]])     
    return ans     
                     
            


















nums = [7, 2, 4]
k = 2
result = sliding_window(nums, k)
print(result,len(result)) 
result.remove(7)
print(result,len(result)) 
 
