def max_subarray(numbers):

    best_sum = 0
    best_start = best_end = 0
    current_sum = 0
    for current_end, x in enumerate(numbers):

        if current_sum <= 0:
            current_start = current_end
            current_sum = x
        else:
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end + 1

    return best_sum, best_start, best_end


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sum, start, end = max_subarray(a)
print(a[start:end])
