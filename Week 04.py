class Solution:
    def threeSumClosest(self, A, B):
        A.sort()
        closest_sum = float('inf')
        min_diff = float('inf')
        n = len(A)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = A[i] + A[left] + A[right]
                current_diff = abs(current_sum - B)

                if current_diff < min_diff:
                    min_diff = current_diff
                    closest_sum = current_sum

                if current_sum < B:
                    left += 1
                elif current_sum > B:
                    right -= 1
                else:
                    return closest_sum

        return closest_sum
