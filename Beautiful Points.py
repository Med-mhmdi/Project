def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def derangements(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    if n == 2:
        return 1
    return (n - 1) * (derangements(n - 1) + derangements(n - 2))


def beautiful_points(n, k):
    choose_k = coefficient(n, k)
    remaining_derangements = derangements(n - k)
    return choose_k * remaining_derangements


n = 5
k = 2
result = beautiful_points(n, k)
print(f"n = {n} k = {k} ==> beautiful points: {result}")

n = 9
k = 6
result = beautiful_points(n, k)
print(f"n = {n} k = {k} ==> beautiful points: {result}")

n = 2
k = 1
result = beautiful_points(n, k)
print(f"n = {n} k = {k} ==> beautiful points: {result}")

n = 9
k = 0
result = beautiful_points(n, k)
print(f"n = {n} k = {k} ==> beautiful points: {result}")
