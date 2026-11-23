"""
Q1: Decomposition and Elimination in Ordered Data
Part A: Finding Maximum and Minimum (Tournament Divide and Conquer)
Part B: Binary Search (Elimination)
"""

def max_min_dc(arr, low, high, counter):
    """
    Tournament divide-and-conquer for finding maximum and minimum.
    Returns (min_val, max_val).
    """
    if low == high:
        return arr[low], arr[low]
    elif high == low + 1:
        counter['comps'] += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
    
    mid = (low + high) // 2
    min1, max1 = max_min_dc(arr, low, mid, counter)
    min2, max2 = max_min_dc(arr, mid + 1, high, counter)
    
    counter['comps'] += 2
    actual_min = min1 if min1 < min2 else min2
    actual_max = max1 if max1 > max2 else max2
    return actual_min, actual_max

def binary_search(arr, target, counter):
    """
    Binary Search on sorted array.
    Returns index if found, else -1.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        counter['comps'] += 1
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == '__main__':
    data = [24, 13, 88, 45, 12, 67, 91, 3, 55, 76, 42, 19, 8, 99, 31, 60]
    c_mm = {'comps': 0}
    mn, mx = max_min_dc(data, 0, len(data) - 1, c_mm)
    print(f"Max-Min Tournament on n={len(data)}: Min = {mn}, Max = {mx}, Comparisons = {c_mm['comps']}")
    print(f"Theoretical Comparisons: 3n/2 - 2 = {int(1.5 * len(data) - 2)}")
    
    sorted_data = sorted(data)
    c_bs_succ = {'comps': 0}
    idx = binary_search(sorted_data, 55, c_bs_succ)
    print(f"Binary Search (Target 55): Found at index {idx}, Comparisons = {c_bs_succ['comps']}")
    
    c_bs_fail = {'comps': 0}
    idx_f = binary_search(sorted_data, 50, c_bs_fail)
    print(f"Binary Search (Target 50 - Missing): Found at index {idx_f}, Comparisons = {c_bs_fail['comps']}")
