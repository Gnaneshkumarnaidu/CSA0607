# Stable Merge Sort – Pseudocode
# Module 1: Nightly Order Consolidation
# KartIQ – Retail Data Analytics Platform | CO3 Case Study

## Algorithm: Stable Merge Sort

### Key Property
Stability is guaranteed by the condition `L[i].timestamp <= R[j].timestamp`
in the merge step. When timestamps are equal, the LEFT element is placed first,
preserving the original arrival order required for audit compliance.

### Time Complexity:  Θ(n log n) — all cases (best, average, worst)
### Space Complexity: O(n) auxiliary memory for temporary arrays


MERGE-SORT(A, left, right):
────────────────────────────
    if left >= right:
        return                          // Base case: single element, already sorted

    mid = ⌊(left + right) / 2⌋         // Integer division; find midpoint

    MERGE-SORT(A, left, mid)            // Conquer: recursively sort left half
    MERGE-SORT(A, mid + 1, right)       // Conquer: recursively sort right half
    MERGE(A, left, mid, right)          // Combine: merge two sorted halves


MERGE(A, left, mid, right):
─────────────────────────────
    n1 ← mid - left + 1                // Number of elements in left half
    n2 ← right - mid                   // Number of elements in right half

    // Allocate temporary arrays
    L[0 .. n1-1]
    R[0 .. n2-1]

    // Copy data to temporary arrays
    for i ← 0 to n1 - 1:
        L[i] ← A[left + i]

    for j ← 0 to n2 - 1:
        R[j] ← A[mid + 1 + j]

    // Merge phase
    i ← 0, j ← 0, k ← left

    while i < n1 AND j < n2:
        //  *** STABILITY CRITICAL: use <=, not < ***
        //  When timestamps are equal, left element goes first → preserves arrival order
        if L[i].timestamp <= R[j].timestamp:
            A[k] ← L[i]
            i ← i + 1
        else:
            A[k] ← R[j]
            j ← j + 1
        k ← k + 1

    // Copy remaining elements from left half (if any)
    while i < n1:
        A[k] ← L[i]
        i ← i + 1
        k ← k + 1

    // Copy remaining elements from right half (if any)
    while j < n2:
        A[k] ← R[j]
        j ← j + 1
        k ← k + 1


### External Merge Sort (when data exceeds RAM)

EXTERNAL-MERGE-SORT(input_file, output_file, RAM_size):
────────────────────────────────────────────────────────
    // Phase 1: Create sorted runs
    run_files ← []
    while input_file has data:
        chunk ← READ(input_file, RAM_size)
        MERGE-SORT(chunk, 0, len(chunk)-1)
        run_file ← WRITE_TEMP_FILE(chunk)
        run_files.append(run_file)

    // Phase 2: K-way merge using min-heap
    heap ← MIN-HEAP()
    for each run_file in run_files:
        record ← READ_FIRST(run_file)
        heap.INSERT((record.timestamp, record, run_file))

    while heap is not empty:
        (timestamp, record, source_file) ← heap.EXTRACT-MIN()
        WRITE(output_file, record)
        next_record ← READ_NEXT(source_file)
        if next_record exists:
            heap.INSERT((next_record.timestamp, next_record, source_file))
