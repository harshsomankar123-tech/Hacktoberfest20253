class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        curr_sum,max_sum,min_sum,curr_min=-inf,-inf,inf,inf
       
        for x in nums:
            curr_sum = max(x,curr_sum + x)
            max_sum = max(max_sum,curr_sum) 
            curr_min = min(x,curr_min + x)
            min_sum = min(min_sum,curr_min)
        if max_sum >0:
                max_sum = max(max_sum,total_sum-min_sum)
                return max_sum
        else:
          return max_sum


