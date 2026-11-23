"""
Q7: Day-4 Design Challenge - Divide and Conquer from First Principles
Problem: Maximum Contiguous Subarray Sum (Kadane-equivalent in D&C O(n log n))
Jointly designed, mathematically validated by Student A, experimentally validated by Student B.
"""

def max_crossing_sum(arr, low, mid, high, counter):
    left_sum = -float('inf')
    cur = 0
    max_left_idx = mid
    for i in range(mid, low - 1, -1):
        counter['ops'] += 1
        cur += arr[i]
        if cur > left_sum:
            left_sum = cur
            max_left_idx = i
            
    right_sum = -float('inf')
    cur = 0
    max_right_idx = mid + 1
    for j in range(mid + 1, high + 1):
        counter['ops'] += 1
        cur += arr[j]
        if cur > right_sum:
            right_sum = cur
            max_right_idx = j
            
    return left_sum + right_sum, max_left_idx, max_right_idx

def max_subarray_dc(arr, low, high, counter):
    if low == high:
        counter['ops'] += 1
        return arr[low], low, high
    
    mid = (low + high) // 2
    left_sum, l_low, l_high = max_subarray_dc(arr, low, mid, counter)
    right_sum, r_low, r_high = max_subarray_dc(arr, mid + 1, high, counter)
    cross_sum, c_low, c_high = max_crossing_sum(arr, low, mid, high, counter)
    
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, l_low, l_high
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, r_low, r_high
    else:
        return cross_sum, c_low, c_high

if __name__ == '__main__':
    test_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    c_q7 = {'ops': 0}
    best_sum, start, end = max_subarray_dc(test_arr, 0, len(test_arr) - 1, c_q7)
    print(f"Max Subarray D&C: Sum = {best_sum}, Subarray = {test_arr[start:end+1]}, Operations = {c_q7['ops']}")
