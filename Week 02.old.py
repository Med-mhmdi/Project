class Solution(object):
    def countPairs(self, nums, target):
        n = len(nums)
        num_pairs = 0
        for i in range(n):
            for j in range(n):
                if i < j and nums[i] + nums[j] < target:
                    num_pairs += 1
        return num_pairs

# not linear time complexity
