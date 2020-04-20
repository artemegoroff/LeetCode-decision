def max_subarray(numbers):

    best_sum = numbers[0]
    left = right = 0
    current_sum = 0
    minus_pos = -1
    for i, value in enumerate(numbers):
        current_sum += value

        if current_sum > best_sum:
            best_sum = current_sum
            left = minus_pos + 1
            right = i+1

        if current_sum < 0:
            current_sum = 0
            minus_pos = i



    return best_sum, left, right


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
a = [-1]
sum, start, end = max_subarray(a)
print(sum, a[start:end])

