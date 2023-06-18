def maxSubArray( nums: list[int]) -> int:
        max = -10000000000
        sum = 0
        for i in range(len(nums)):
            if sum == 0:
                s =i
            sum = sum +nums[i]
            if sum >max:
                max = sum
                s_ans = s
                s_end = i
            if sum <0:
                sum =0
            
        return max , nums[s_ans:s_end]
a,b = maxSubArray([-2,-3,4,-1,-2,1,5,-3])        
print(a,b)
