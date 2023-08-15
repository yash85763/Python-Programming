def findMaxAverage(nums, k):
        curr = 0
        avg = 0
        if k == 1:
            return sum(nums)/1
        
        for i in range(k):
            curr  += nums[i]
        ans = curr
        
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            ans = max(ans, curr)
            avg = ans/k
        return avg
findMaxAverage([5], 1)
