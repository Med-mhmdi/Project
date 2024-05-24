def min_ele_to_flip(A):
    total_sum = sum(A)
    target = total_sum // 2

    dp = [0] * (target + 1)
    dp[0] = 1

    for num in A:
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True

    for i in range(target, -1, -1):
        if dp[i]:
            closest_sum = i
            break

    min_non_negative_sum = total_sum - 2 * closest_sum

    half_diff = (total_sum - min_non_negative_sum) // 2
    elements_to_flip = []
    remaining_sum = half_diff
    for num in A:
        if remaining_sum >= num and (remaining_sum - num) in dp:
            elements_to_flip.append(num)
            remaining_sum -= num

    return len(elements_to_flip)


A1 = [15, 10, 6]
A2 = [14, 10, 4]

print(f"min element to flip sign for A1 is: {min_ele_to_flip(A1)}")
print(f"min element to flip sign for A2 is: {min_ele_to_flip(A2)}")
