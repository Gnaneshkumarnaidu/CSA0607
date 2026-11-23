# Improved Quick Sort – Pseudocode
# Module 2: Live Seller Leaderboard
# KartIQ – Retail Data Analytics Platform | CO3 Case Study

## Algorithm: Quick Sort with Median-of-Three Pivot + Three-Way Partitioning

### Key Properties
- Median-of-Three pivot: eliminates worst case on sorted/nearly-sorted input
- Three-way partitioning: handles equal scores efficiently (common during sale events)
- In-place: O(log n) auxiliary space (call stack only)

### Time Complexity:  Θ(n log n) average/expected case
### Space Complexity: O(log n) — recursion stack depth


QUICKSORT-IMPROVED(A, low, high):
──────────────────────────────────
    if low < high:
        // Step 1: Select pivot using Median-of-Three
        pivot_idx ← MEDIAN-OF-THREE-INDEX(A, low, high)
        swap(A[pivot_idx], A[high])        // Move pivot to end for partitioning

        // Step 2: Three-way partition (handles equal scores)
        lt, gt ← THREE-WAY-PARTITION(A, low, high)
        //  After partition:
        //    A[low .. lt-1]  all < pivot
        //    A[lt  .. gt]    all = pivot  ← final positions, no recursion needed
        //    A[gt+1 .. high] all > pivot

        // Step 3: Recursively sort only the non-equal regions
        QUICKSORT-IMPROVED(A, low, lt - 1)
        QUICKSORT-IMPROVED(A, gt + 1, high)


MEDIAN-OF-THREE-INDEX(A, low, high):
─────────────────────────────────────
    mid ← ⌊(low + high) / 2⌋

    // Sort A[low], A[mid], A[high] so that A[mid] is the median
    if A[low].score > A[mid].score:  swap(A[low], A[mid])
    if A[low].score > A[high].score: swap(A[low], A[high])
    if A[mid].score > A[high].score: swap(A[mid], A[high])

    // After sorting these three: A[low] ≤ A[mid] ≤ A[high]
    // A[mid] is the median
    return mid


THREE-WAY-PARTITION(A, low, high):
────────────────────────────────────
    pivot ← A[high].score
    lt ← low        // A[low .. lt-1] < pivot
    gt ← high       // A[gt+1 .. high] > pivot
    i ← low         // Current element under examination

    while i <= gt:
        if A[i].score < pivot:
            swap(A[lt], A[i])
            lt ← lt + 1
            i  ← i  + 1
        else if A[i].score > pivot:
            swap(A[i], A[gt])
            gt ← gt - 1
            // Do NOT increment i — newly swapped element needs examination
        else:  // A[i].score == pivot
            i ← i + 1

    return lt, gt    // A[lt..gt] all equal to pivot


### Standard Quick Sort (for reference — do NOT use for nearly-sorted input)

QUICKSORT-NAIVE(A, low, high):
────────────────────────────────
    if low < high:
        pivot_idx ← PARTITION-NAIVE(A, low, high)
        QUICKSORT-NAIVE(A, low, pivot_idx - 1)
        QUICKSORT-NAIVE(A, pivot_idx + 1, high)

PARTITION-NAIVE(A, low, high):
    pivot ← A[low].score     // BAD: first element, O(n²) on sorted input
    i ← high + 1
    for j ← high downto low + 1:
        if A[j].score >= pivot:
            i ← i - 1
            swap(A[i], A[j])
    swap(A[low], A[i-1])
    return i - 1
