import heapq

def n_ropes_min_cost(a):
    heapq.heapify(a)
    print(a)
    ans = 0
    while len(a) > 1:
        first = heapq.heappop(a) 
        second =heapq.heappop(a)
        summ = first + second
        ans += summ
        heapq.heappush(a,summ)
    return ans

a = [2,5,4,8,6,9]
print(n_ropes_min_cost(a))
    


    
