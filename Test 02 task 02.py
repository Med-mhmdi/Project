def diplomas(side_length, w, h, n):
    max_diplomas_per_row = side_length // w
    max_diplomas_per_column = side_length // h
    total_diplomas = max_diplomas_per_row * max_diplomas_per_column
    return total_diplomas >= n

def min_board_size(w, h, n):
    left = 1
    right = max(w, h) * n
    while left < right:
        mid = (left + right) // 2
        if diplomas(mid, w, h, n):
            right = mid
        else:
            left = mid + 1
    return left

w = 3
h = 2
n = 10
print(f'{min_board_size(w, h, n)} unity square')
