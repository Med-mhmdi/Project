def back(N, weights):
    def combinations(x, pile_weight):
        if x == N:
            return abs(total_weight - 2 * pile_weight)
        return min(
            combinations(x + 1, pile_weight + weights[x]),
            combinations(x + 1, pile_weight)
        )

    total_weight = sum(weights)
    return combinations(0, 0)


weights = [1, 2, 5, 4, 1]
n = len(weights)

if 1 <= n <= 18 and 1 <= sum(weights) <= 105:
    print(back(n, weights))
else:
    print("Out of range")
