"""
Q2: The Quality of Decomposition in Sorting
Comparative study: Merge Sort vs Quick Sort
Investigating recursion tree depth, partitioning quality, and comparisons.
"""
import sys

def merge_sort(arr, counter):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], counter)
    right = merge_sort(arr[mid:], counter)
    
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        counter['comps'] += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def quick_sort(arr, low, high, counter, depth=0):
    if depth > counter['max_depth']:
        counter['max_depth'] = depth
    if low < high:
        pivot_idx = partition(arr, low, high, counter)
        quick_sort(arr, low, pivot_idx - 1, counter, depth + 1)
        quick_sort(arr, pivot_idx + 1, high, counter, depth + 1)

def partition(arr, low, high, counter):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        counter['comps'] += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

if __name__ == '__main__':
    # Balanced (Random) Input
    import random
    n = 16
    random.seed(42)
    rand_data = random.sample(range(1, 100), n)
    
    c_ms = {'comps': 0}
    sorted_ms = merge_sort(list(rand_data), c_ms)
    print(f"Merge Sort on n={n}: Comps = {c_ms['comps']}")
    
    c_qs_rand = {'comps': 0, 'max_depth': 0}
    qs_rand_arr = list(rand_data)
    quick_sort(qs_rand_arr, 0, n - 1, c_qs_rand)
    print(f"Quick Sort Balanced (Random) on n={n}: Comps = {c_qs_rand['comps']}, Max Depth = {c_qs_rand['max_depth']}")
    
    # Adversarial (Sorted) Input - Degenerate O(n^2)
    c_qs_adv = {'comps': 0, 'max_depth': 0}
    qs_adv_arr = list(range(1, n + 1))
    quick_sort(qs_adv_arr, 0, n - 1, c_qs_adv)
    print(f"Quick Sort Unbalanced (Sorted Array) on n={n}: Comps = {c_qs_adv['comps']}, Max Depth = {c_qs_adv['max_depth']}")
