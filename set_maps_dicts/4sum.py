def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    n = len(nums)
    st = set()
    # checking all possible quadruplets:
    for i in range(n):
        for j in range(i+1, n):
            hashset = set()
            for k in range(j+1, n):
                # taking bigger data type to avoid integer overflow:
                sum_ = nums[i] + nums[j] + nums[k]
                fourth = target - sum_
                if fourth in hashset:
                    temp = [(nums[i], nums[j], nums[k], fourth)]
                    temp.sort()
                    st.add(tuple(temp))
            # put the kth element into the hashset:
            hashset.add(nums[k])

    ans = [list(t) for t in st]
    return ans
def optimal(nums,target):
    n = len(nums) # size of the array
    ans = []
    # sort the given array:
    nums.sort()
    # calculating the quadruplets:
    for i in range(n):
        # avoid the duplicates while moving i:
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            # avoid the duplicates while moving j:
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            # 2 pointers:
            k = j + 1
            l = n - 1
            while k < l:
                _sum = nums[i] + nums[j] + nums[k] + nums[l]
                if _sum == target:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    ans.append(temp)
                    k += 1
                    l -= 1
                    # skip the duplicates:
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                elif _sum < target:
                    k += 1
                else:
                    l -= 1
    return ans