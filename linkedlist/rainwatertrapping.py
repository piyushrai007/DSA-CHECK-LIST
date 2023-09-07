def bruteforce(height):
    a = 0
    n = len(height)
    for i in range(n):
        a +=(min(max(height[0:i+1]),max(height[i:n]))-height[i])
    return a
def better(height):
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    a = 0
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])
    for i in range(n):
        a +=(min(left_max[i],right_max[i])-height[i])


    return a
def optimal(height,n):
    l =0
    r= n-1
    trap =0 
    left_max= 0
    right_max =0
    while l<=r:
        if height[l]<=height[r]:
            if height[l]>=left_max:
                left_max = height[l]
            else:
                trap += (left_max -height[l])
            l +=1      
        else:
            if height[r]>=right_max:
                right_max = height[r]
            else:
                trap += (right_max -height[r])
            r-=1    
    return trap     
height = [0,1,0,2,1,0,1,3,2,1,2,1]
n = len (height)
print(optimal(height,n))