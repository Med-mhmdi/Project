class Solution:
    def solve(self, A, B):
        left = 0
        max_length = 0
        zero_count = 0

        for right in range(len(A)):
            if A[right] == 0:
                zero_count += 1

            while zero_count > B:
                if A[left] == 0:
                    zero_count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

#Correct
