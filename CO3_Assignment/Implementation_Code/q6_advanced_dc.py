"""
Q6: Advanced Divide and Conquer Mini-Investigations
Student A: Median of Medians (Deterministic O(n) Selection)
Student B: Meet-in-the-Middle (Subset Sum Reduction from O(2^n) to O(2^(n/2)))
"""
import bisect

# --- Part A: Median of Medians ---
def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    
    # Divide into groups of 5
    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(sub)[len(sub)//2] for sub in sublists]
    
    pivot = median_of_medians(medians, len(medians)//2)
    
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(pivots):
        return pivot
    else:
        return median_of_medians(high, k - len(low) - len(pivots))

# --- Part B: Meet in the Middle ---
def get_subset_sums(arr):
    sums = [0]
    for x in arr:
        sums += [s + x for s in sums]
    return sorted(sums)

def meet_in_the_middle_subset_sum(arr, target):
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left_sums = get_subset_sums(left)
    right_sums = get_subset_sums(right)
    
    # Binary search right_sums for target - s
    for s in left_sums:
        req = target - s
        idx = bisect.bisect_left(right_sums, req)
        if idx < len(right_sums) and right_sums[idx] == req:
            return True
    return False

if __name__ == '__main__':
    data = [12, 3, 5, 7, 4, 19, 26, 1, 9, 15, 8, 22, 11]
    k = 5
    kth_val = median_of_medians(data, k)
    print(f"Median of Medians ({k}-th smallest / 0-indexed): {kth_val} (Check sorted: {sorted(data)[k]})")
    
    set_s = [3, 34, 4, 12, 5, 2, 7, 18, 21, 14, 10, 16]
    target = 39
    found = meet_in_the_middle_subset_sum(set_s, target)
    print(f"Meet-in-the-Middle Subset Sum: Target {target} possible? {found}")
