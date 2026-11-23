# Binary Search (Standard + Lower-Bound) – Pseudocode
# Module 3: Order Lookup
# KartIQ – Retail Data Analytics Platform | CO3 Case Study

## Algorithm: Iterative Binary Search + Lower-Bound (First-Occurrence) Variant

### Prerequisite: Input array MUST be sorted (provided by Module 1 – Merge Sort)

### Time Complexity:  Θ(log n) — all cases
### Space Complexity: O(1) — iterative, no recursion stack


BINARY-SEARCH(A, n, target_timestamp):
────────────────────────────────────────
    // Standard Binary Search — returns ANY matching index
    low  ← 0
    high ← n - 1

    while low <= high:
        mid ← ⌊(low + high) / 2⌋      // Integer division

        if A[mid].timestamp == target_timestamp:
            return mid                  // Found — returns any occurrence

        else if A[mid].timestamp < target_timestamp:
            low ← mid + 1              // Target is in right half

        else:                           // A[mid].timestamp > target
            high ← mid - 1             // Target is in left half

    return -1                           // Not found


BINARY-SEARCH-LOWER-BOUND(A, n, target_timestamp):
────────────────────────────────────────────────────
    // First-Occurrence Binary Search
    // Returns index of FIRST element with timestamp == target
    // Essential for audit trail: earlier arrival order preserved by Module 1
    
    low    ← 0
    high   ← n - 1
    result ← -1                        // Initialize: not found

    while low <= high:
        mid ← ⌊(low + high) / 2⌋

        if A[mid].timestamp == target_timestamp:
            result ← mid               // Record this match
            high   ← mid - 1          // KEY: continue searching LEFT for earlier occurrence

        else if A[mid].timestamp < target_timestamp:
            low ← mid + 1

        else:
            high ← mid - 1

    return result
    // If result == -1 → timestamp not in array
    // Otherwise → index of FIRST occurrence (smallest index with matching timestamp)


BINARY-SEARCH-UPPER-BOUND(A, n, target_timestamp):
────────────────────────────────────────────────────
    // Last-Occurrence Binary Search
    // Returns index of LAST element with timestamp == target
    
    low    ← 0
    high   ← n - 1
    result ← -1

    while low <= high:
        mid ← ⌊(low + high) / 2⌋

        if A[mid].timestamp == target_timestamp:
            result ← mid
            low    ← mid + 1          // KEY: continue searching RIGHT for later occurrence

        else if A[mid].timestamp < target_timestamp:
            low ← mid + 1

        else:
            high ← mid - 1

    return result


### Usage for KartIQ Order Lookup

GET-ALL-ORDERS-BY-TIMESTAMP(A, n, target_timestamp):
──────────────────────────────────────────────────────
    // Retrieve all orders with a given timestamp
    first ← BINARY-SEARCH-LOWER-BOUND(A, n, target_timestamp)
    if first == -1:
        return []                      // No orders with this timestamp

    last ← BINARY-SEARCH-UPPER-BOUND(A, n, target_timestamp)
    return A[first .. last]            // All orders in range [first, last]
