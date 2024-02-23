class Solution(object):
    def countKDifference(self, nums, k):
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        count = 0

        for num in frequency_map:
            if k > 0 and num + k in frequency_map:
                count += frequency_map[num] * frequency_map[num + k]
            elif k == 0 and frequency_map[num] > 1:
                count += frequency_map[num] * (frequency_map[num] - 1) // 2

        return count
