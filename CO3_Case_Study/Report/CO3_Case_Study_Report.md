# KartIQ – Retail Data Analytics Platform
## CO3 Case Study Assignment

---

<div align="center">

# VELAMMAL COLLEGE OF ENGINEERING AND TECHNOLOGY
### Department of Computer Science and Engineering

---

**Subject:** Design and Analysis of Algorithms  
**Course Code:** CSA0607  
**Assessment:** CO3 – Case Study  
**Topic:** Divide-and-Conquer Engine of a Retail Data Analytics Platform  
**Case Study Name:** KartIQ – Retail Data Analytics Platform  
**Duration:** 1 Week  
**Mode:** Individual  

---

**Student Name:** M.Gnanesh kumar naidu  
**Registration Number:** 192371051  
**Signature:** ______________________  
**Date:** 15-11-2026  

---

*Submitted in partial fulfillment of the requirements for CO3 Assessment*  
*Academic Year: 2024–2025*

</div>

---

## TABLE OF CONTENTS

1. [Introduction](#1-introduction)
2. [Question (a) – Understanding the Case](#2-question-a--understanding-the-case)
3. [Question (b) – Module 1: Merge Sort – Nightly Order Consolidation](#3-question-b--module-1-merge-sort--nightly-order-consolidation)
4. [Question (c) – Module 2: Quick Sort – Live Seller Leaderboard](#4-question-c--module-2-quick-sort--live-seller-leaderboard)
5. [Question (d) – Module 3: Binary Search – Order Lookup](#5-question-d--module-3-binary-search--order-lookup)
6. [Question (e) – Module 4: Strassen's Matrix Multiplication – Recommendation Scores](#6-question-e--module-4-strassens-matrix-multiplication--recommendation-scores)
7. [Question (f) – Final System Design and Justification](#7-question-f--final-system-design-and-justification)
8. [Overall Conclusion](#8-overall-conclusion)
9. [References](#9-references)
10. [Student Declaration](#10-student-declaration)

---

## 1. INTRODUCTION

### 1.1 Background

E-commerce platforms today process enormous volumes of data every second. As platforms scale from thousands to millions of users, the choice of algorithm becomes a critical engineering decision — not merely an academic one. A poorly chosen algorithm that runs in O(n²) time can freeze an entire system during a peak sale event, while a well-chosen O(n log n) algorithm handles the same load seamlessly.

KartIQ is a mid-to-large-scale retail data analytics platform that faces exactly this kind of challenge. Each day, the platform:
- Consolidates millions of nightly orders from multiple regional warehouses.
- Maintains a real-time seller leaderboard that updates rapidly during flash sales.
- Provides instant order lookup for customer support teams.
- Computes collaborative-filtering recommendation scores using matrix operations.

Each of these four operations is a distinct computational problem with its own constraints, data characteristics, and performance requirements. This case study examines how **Divide-and-Conquer** algorithms can be applied to solve each problem efficiently, and how selecting the right algorithm — with the right configuration — determines the difference between a platform that scales gracefully and one that collapses under load.

### 1.2 Why Divide and Conquer?

The divide-and-conquer paradigm follows three steps:
1. **Divide:** Break the problem into smaller subproblems of the same type.
2. **Conquer:** Solve each subproblem recursively.
3. **Combine:** Merge the subproblem solutions to obtain the final answer.

This approach is particularly effective when:
- The problem has optimal substructure (the solution to the whole can be built from solutions to parts).
- Subproblems are independent of each other.
- The cost of dividing and combining is manageable relative to the savings from smaller subproblems.

For KartIQ, divide-and-conquer algorithms such as Merge Sort, Quick Sort, Binary Search, and Strassen's Matrix Multiplication are ideal because they achieve significantly better time complexities than their naive counterparts — transforming O(n²) or O(n³) solutions into O(n log n) or O(n^2.807) solutions that remain practical at scale.

---

## 2. QUESTION (a) – UNDERSTANDING THE CASE

### 2.1 Module-wise Analysis Table

The following table summarises the computational requirements, algorithm choices, key challenges, constraints, and consequences for each of KartIQ's four operational modules.

| **Aspect** | **Module 1: Nightly Order Consolidation** | **Module 2: Live Seller Leaderboard** | **Module 3: Order Lookup** | **Module 4: Recommendation Scores** |
|---|---|---|---|---|
| **Algorithm Selected** | Stable Merge Sort | Quick Sort (Improved) | Binary Search (Lower-Bound) | Strassen's Matrix Multiplication |
| **Computational Requirement** | Sort ~10 million orders nightly by timestamp from multiple regional databases | Sort ~100,000 seller scores in real-time during flash sales | Search for a specific order ID or timestamp in a sorted list of ~10 million records | Multiply large item–user and user–feature matrices for collaborative filtering |
| **Key Technical Challenge** | Preserving original arrival order for orders with identical timestamps (audit compliance); merging data from multiple regional sources | Pivot selection causing worst-case O(n²) on nearly sorted data during peak events; stack overflow risk on large input | Ensuring the array is pre-sorted; returning the **first** occurrence when duplicate timestamps exist | Cubic complexity O(n³) of conventional multiplication is too slow for large matrices |
| **Important Constraints** | Must be **stable** (equal keys retain original order); must handle data exceeding RAM (external sort may be needed); must complete within nightly batch window | Must complete in near real-time (<1 second per update); must handle equal scores correctly | Requires pre-sorted input (dependency on Module 1); must handle duplicate timestamps | Matrices may not be powers of 2 (padding required); floating-point precision issues; overhead for small matrices |
| **Consequence of Unsuitable Algorithm** | Using unstable sort (e.g., standard Quick Sort) violates audit requirements — orders with the same timestamp would be reordered arbitrarily, making audit trails invalid | Using naive first-element pivot on nearly sorted data degrades to O(n²), causing the leaderboard to freeze for minutes during sale events | Using linear search O(n) on 10M records takes ~10M comparisons; too slow for real-time customer support | Using conventional O(n³) multiplication on large matrices (e.g., 1024×1024) becomes infeasible within response time budgets |

### 2.2 Role of Divide and Conquer in Solving Platform Problems

**Divide and Conquer** is the unifying design principle behind all four modules. Here is how it addresses the platform's specific performance challenges:

**Problem 1 – Scale of Data (Millions of Records)**  
Brute-force approaches (Bubble Sort, Selection Sort, Linear Search) have O(n²) or O(n) complexities that are simply unacceptable at the scale of 10 million records. Divide-and-conquer algorithms reduce the problem size logarithmically at each recursion level, bringing time complexity down to O(n log n) or O(log n).

**Problem 2 – Real-Time Performance Requirements**  
During a flash sale, the seller leaderboard must update in under a second. Quick Sort's average-case O(n log n) performance, achieved through divide-and-conquer partitioning, makes this possible — provided the pivot is chosen wisely.

**Problem 3 – Audit and Correctness Requirements**  
The divide-and-conquer Merge Sort is inherently stable — it preserves the relative order of equal elements because the merge step copies the left-side element first on ties. This stability is not incidental; it is a direct consequence of the algorithm's combine step, which makes it the only correct choice for the audit-sensitive Module 1.

**Problem 4 – Matrix Computation Efficiency**  
Strassen's algorithm reduces the number of recursive subproblem calls from 8 (conventional) to 7 by performing additional additions/subtractions. This reduces the exponent from log₂8 = 3 to log₂7 ≈ 2.807, yielding a meaningful speedup for large matrices.

In summary, Divide and Conquer transforms infeasible O(n²) and O(n³) computations into tractable O(n log n) and O(n^2.807) operations, directly addressing KartIQ's bottlenecks at scale.

---

## 3. QUESTION (b) – MODULE 1: MERGE SORT – NIGHTLY ORDER CONSOLIDATION

### 3.1 Why Merge Sort?

KartIQ's nightly consolidation must sort approximately 10 million orders by timestamp. The critical requirement is **stability**: if two orders carry the same timestamp, the one that arrived first (earlier in the input) must appear first in the output. This is an audit requirement — financial regulators and internal auditing systems rely on this ordering to verify transaction sequences.

Merge Sort satisfies all requirements for this module:
1. **Stable:** Equal elements are never swapped; the left subarray always takes precedence on ties.
2. **Guaranteed O(n log n):** Unlike Quick Sort, Merge Sort's worst case is also O(n log n).
3. **Parallelisable:** Data from multiple regional warehouses can be sorted independently and then merged — a natural fit for the divide-and-conquer structure.

### 3.2 Algorithm Explanation

**Divide:**  
The input array of n orders is split into two halves of size n/2 and n/2 (ceiling for odd sizes). No comparison is made during division.

**Conquer:**  
Each half is recursively sorted using the same Merge Sort procedure. The base case is a single-element array, which is already sorted by definition.

**Combine (Merge):**  
Two sorted subarrays are merged into one sorted array. During merging, elements are compared one by one. When two elements are equal (same timestamp), the element from the **left subarray is always placed first**. This is the key to stability.

### 3.3 Why Stability is Essential

Consider two orders with timestamp 102:
- O2 arrived first → should appear before O5 in audit logs.

An unstable sort might produce: ..., (102, O5), (102, O2), ... — reversing their order, making it appear that O5 was processed before O2. This violates the audit chain and can cause compliance failures.

Stable Merge Sort guarantees: ..., (102, O2), (102, O5), ... — preserving arrival order.

### 3.4 Step-by-Step Execution on Sample Data

**Initial Array (timestamp, order_id):**

```
Index:  0        1        2        3        4        5
Data: (105,O1) (102,O2) (105,O3) (101,O4) (102,O5) (103,O6)
```

**Step 1 – Division Phase**

```
Level 0:  [(105,O1) (102,O2) (105,O3) (101,O4) (102,O5) (103,O6)]
           __________________________|___________________________
          /                                                      \
Level 1: [(105,O1) (102,O2) (105,O3)]         [(101,O4) (102,O5) (103,O6)]
          ___________|___________               ___________|___________
         /                       \             /                       \
Level 2: [(105,O1) (102,O2)]  [(105,O3)]   [(101,O4) (102,O5)]  [(103,O6)]
          ________|_______                   ________|_______
         /                 \               /                 \
Level 3: [(105,O1)]   [(102,O2)]      [(101,O4)]        [(102,O5)]
```

At Level 3, all subarrays are single elements — the base case. Recursion bottoms out here.

**Step 2 – Merge Phase (bottom-up)**

**Merge 1:** `[(105,O1)]` and `[(102,O2)]`
- Compare 105 vs 102 → 102 < 105 → place (102,O2)
- Remaining: (105,O1)
- Result: **`[(102,O2) (105,O1)]`**

**Merge 2:** Result of Merge 1 with `[(105,O3)]`
- Merge `[(102,O2) (105,O1)]` and `[(105,O3)]`
- Compare (102,O2) vs (105,O3) → 102 < 105 → place (102,O2)
- Compare (105,O1) vs (105,O3) → **equal timestamps (105 = 105)** → place left = (105,O1) ← **stability preserved**
- Remaining: (105,O3)
- Result: **`[(102,O2) (105,O1) (105,O3)]`**

**Merge 3:** `[(101,O4)]` and `[(102,O5)]`
- Compare 101 vs 102 → 101 < 102 → place (101,O4)
- Remaining: (102,O5)
- Result: **`[(101,O4) (102,O5)]`**

**Merge 4:** Result of Merge 3 with `[(103,O6)]`
- Merge `[(101,O4) (102,O5)]` and `[(103,O6)]`
- Compare (101,O4) vs (103,O6) → 101 < 103 → place (101,O4)
- Compare (102,O5) vs (103,O6) → 102 < 103 → place (102,O5)
- Remaining: (103,O6)
- Result: **`[(101,O4) (102,O5) (103,O6)]`**

**Final Merge (Level 0):** `[(102,O2) (105,O1) (105,O3)]` and `[(101,O4) (102,O5) (103,O6)]`

| Step | Left Pointer | Right Pointer | Comparison | Action | Output so far |
|------|-------------|--------------|------------|--------|---------------|
| 1 | (102,O2) | (101,O4) | 102 > 101 | Place right (101,O4) | (101,O4) |
| 2 | (102,O2) | (102,O5) | 102 = 102 | **Equal → Place left (102,O2)** ← stability | (101,O4)(102,O2) |
| 3 | (105,O1) | (102,O5) | 105 > 102 | Place right (102,O5) | ...(102,O5) |
| 4 | (105,O1) | (103,O6) | 105 > 103 | Place right (103,O6) | ...(103,O6) |
| 5 | (105,O1) | — | Right exhausted | Place all remaining left | (105,O1)(105,O3) |

**Final Sorted Output:**

```
[(101,O4) (102,O2) (102,O5) (103,O6) (105,O1) (105,O3)]
```

**Stability Verification:**
- (102,O2) appears before (102,O5) ✅ — O2 arrived first, correctly preserved.
- (105,O1) appears before (105,O3) ✅ — O1 arrived first, correctly preserved.

### 3.5 Mathematical Analysis

#### 3.5.1 Recurrence Relation

Merge Sort divides n elements into two halves, sorts each recursively, and merges in Θ(n) time:

```
T(n) = 2T(n/2) + Θ(n),    T(1) = Θ(1)
```

#### 3.5.2 Solution via Master Theorem

The recurrence is in the form T(n) = aT(n/b) + f(n) where:
- a = 2 (two recursive calls)
- b = 2 (each call processes half the input)
- f(n) = Θ(n) (linear merge step)

Compute n^(log_b a) = n^(log₂ 2) = n^1 = n.

Since f(n) = Θ(n) = Θ(n^(log₂ 2)), we apply **Master Theorem Case 2:**

> When f(n) = Θ(n^(log_b a)), the solution is T(n) = **Θ(n^(log_b a) · log n)**

Therefore:

```
T(n) = Θ(n · log n) = Θ(n log n)
```

#### 3.5.3 Recursion Tree Verification

At level 0: 1 subproblem of size n → merge cost = cn  
At level 1: 2 subproblems of size n/2 → merge cost = 2 · c(n/2) = cn  
At level 2: 4 subproblems of size n/4 → merge cost = 4 · c(n/4) = cn  
...  
At level k: 2^k subproblems of size n/2^k → merge cost = cn  

Total levels = log₂n (since the problem halves at each level).  
Total work = cn · log₂n = **Θ(n log n)** ✅

#### 3.5.4 Comparison Estimate for 10,000,000 Orders

Using the formula: Comparisons ≈ n · log₂(n)

For n = 10,000,000:
- log₂(10,000,000) = log₂(10^7) = 7 · log₂(10) ≈ 7 × 3.3219 ≈ **23.25**
- Estimated comparisons ≈ 10,000,000 × 23.25 ≈ **232,500,000 comparisons**

This is approximately 232 million comparisons — computed in a matter of seconds on modern hardware, well within the nightly batch window.

#### 3.5.5 Auxiliary Memory Requirement: O(n)

Merge Sort requires a temporary array of size n during the merge step to hold the merged output before writing back to the original array. This is an **O(n) auxiliary space requirement**.

This is distinct from the total memory (input array + auxiliary = 2n), but the extra memory needed beyond the input is O(n).

**Note:** In-place Merge Sort variants exist but are significantly more complex and typically run slower in practice due to increased cache misses.

#### 3.5.6 External Merge Sort

When 10 million orders cannot fit into RAM (e.g., each order record is 500 bytes → 5 GB), **External Merge Sort** is used:

1. **Phase 1 – Run Creation:** Read as much data as fits in RAM, sort it internally using Merge Sort, write the sorted chunk ("run") to disk.
2. **Phase 2 – K-way Merge:** Use a priority queue (min-heap) to simultaneously merge k sorted runs from disk into one final sorted file.
3. **I/O Complexity:** O((n/B) · log_{M/B}(n/B)) where B = disk block size, M = RAM size.

This extends divide-and-conquer naturally to data that exceeds memory capacity.

### 3.6 Pseudocode – Stable Merge Sort

```
MERGE-SORT(A, left, right):
    if left >= right:
        return                          // Base case: single element
    
    mid = (left + right) / 2           // Integer division
    MERGE-SORT(A, left, mid)           // Conquer left half
    MERGE-SORT(A, mid+1, right)        // Conquer right half
    MERGE(A, left, mid, right)         // Combine

MERGE(A, left, mid, right):
    n1 = mid - left + 1                // Size of left subarray
    n2 = right - mid                   // Size of right subarray
    
    // Create temporary arrays L[0..n1-1] and R[0..n2-1]
    for i = 0 to n1-1:
        L[i] = A[left + i]
    for j = 0 to n2-1:
        R[j] = A[mid + 1 + j]
    
    i = 0, j = 0, k = left
    
    while i < n1 AND j < n2:
        // KEY: use <= for stability — left wins on ties
        if L[i].timestamp <= R[j].timestamp:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k = k + 1
    
    // Copy remaining elements
    while i < n1:
        A[k] = L[i]; i++; k++
    while j < n2:
        A[k] = R[j]; j++; k++
```

**Critical Note:** The condition `L[i].timestamp <= R[j].timestamp` (using `<=` not `<`) is what guarantees stability. When timestamps are equal, the left element is placed first, preserving original arrival order.

---

## 4. QUESTION (c) – MODULE 2: QUICK SORT – LIVE SELLER LEADERBOARD

### 4.1 Working Principle

Quick Sort is an in-place, divide-and-conquer sorting algorithm. It works as follows:

1. **Choose a pivot** element from the array.
2. **Partition:** Rearrange the array so that all elements less than the pivot come before it, and all elements greater come after it. The pivot is now in its final sorted position.
3. **Recursively sort** the left partition (elements < pivot) and the right partition (elements > pivot).

The key insight: after partitioning, the pivot never needs to move again. Each recursive call deals with a strictly smaller subproblem.

### 4.2 Partitioning Process

**Convention used:** Lomuto partition scheme. The pivot is placed at the end, and a pointer `i` tracks the boundary between "small" and "large" elements.

```
PARTITION(A, low, high):
    pivot = A[high]          // Last element as pivot
    i = low - 1              // Boundary pointer
    
    for j = low to high-1:
        if A[j] <= pivot:
            i = i + 1
            swap(A[i], A[j])
    
    swap(A[i+1], A[high])    // Place pivot in final position
    return i + 1             // Return pivot index
```

For the trace below, we use the **first element as the pivot** as stated in the problem, using a Hoare-style partitioning for illustration clarity.

### 4.3 Partition Trace – Sample Data

**Input array:** `42, 17, 63, 8, 55, 29`  
**Pivot = 42** (first element)

**Convention:** We scan from both ends. Left pointer `L` moves right past elements ≤ pivot. Right pointer `R` moves left past elements > pivot. When both stop, we swap. When L ≥ R, partition is complete; swap pivot with A[R].

| Step | Array State | L | R | Action |
|------|------------|---|---|--------|
| Initial | **[42]**, 17, 63, 8, 55, 29 | 1 | 5 | Pivot = 42, L starts at index 1, R at index 5 |
| Step 1 | 42, **17**, 63, 8, 55, 29 | L=1 (17≤42, advance) | R=5 | L moves to 2 |
| Step 2 | 42, 17, **63**, 8, 55, 29 | L=2 (63>42, stop) | R=5 | L stops at 2 |
| Step 3 | 42, 17, 63, 8, 55, **29** | L=2 | R=5 (29≤42, stop from right) | R stops at 5 |
| Swap | Swap A[2] and A[5] | — | — | Array: 42, 17, **29**, 8, 55, **63** |
| Step 4 | 42, 17, 29, **8**, 55, 63 | L=3 (8≤42, advance to 4) | R=4 | L moves to 4 |
| Step 5 | 42, 17, 29, 8, **55**, 63 | L=4 (55>42, stop) | R=4 | L stops at 4 |
| Step 6 | 42, 17, 29, 8, **55**, 63 | L=4 | R=4 (55>42, move left to 3) | R stops at 3 |
| L≥R | — | L=4 ≥ R=3 | — | Partition done. Swap pivot (A[0]=42) with A[R=3]=8 |
| Result | **8**, 17, 29, **42**, 55, 63 | — | — | Pivot 42 is in final position (index 3) |

**After partition:**
```
Left partition:  [8, 17, 29]   (all ≤ 42)
Pivot:            42            (in final position)
Right partition: [55, 63]      (all > 42)
```

Recursively apply Quick Sort to `[8, 17, 29]` and `[55, 63]` to obtain the final sorted array: `[8, 17, 29, 42, 55, 63]`.

### 4.4 Why First-Element Pivot Causes Poor Performance on Nearly Sorted Data

If the input array is already sorted or nearly sorted (e.g., `[8, 17, 29, 42, 55, 63]`), and we always pick the first element as the pivot:

- Pivot = 8 (minimum of the array)
- Left partition: empty (0 elements)
- Right partition: [17, 29, 42, 55, 63] (5 elements)

The partition is maximally unbalanced (0 vs n-1 elements). This happens at every recursion level:
- T(n) = T(0) + T(n-1) + Θ(n) = **T(n-1) + Θ(n)**

This yields O(n²) time — the worst case. For 100,000 sellers in a nearly sorted arrangement, this means approximately 100,000²/2 = **5 × 10⁹ comparisons**, which explains why the leaderboard freezes during sale events.

### 4.5 Mathematical Analysis

#### 4.5.1 Best-Case Recurrence

The best case occurs when the pivot always partitions the array exactly in half:

```
T(n) = 2T(n/2) + Θ(n),    T(1) = Θ(1)
```

By Master Theorem (same as Merge Sort — Case 2):
```
T(n) = Θ(n log n)
```

#### 4.5.2 Worst-Case Recurrence

The worst case occurs when the pivot is always the minimum or maximum (maximally unbalanced partition):

```
T(n) = T(n-1) + Θ(n),    T(1) = Θ(1)
```

**Solving by expansion (telescoping):**
```
T(n) = T(n-1) + cn
     = T(n-2) + c(n-1) + cn
     = T(n-3) + c(n-2) + c(n-1) + cn
     ...
     = T(1) + c·2 + c·3 + ... + c·n
     = Θ(1) + c · (2 + 3 + ... + n)
     = Θ(1) + c · (n(n+1)/2 - 1)
     = Θ(n²)
```

Therefore: **T(n) = Θ(n²)** in the worst case.

#### 4.5.3 Comparisons for 100,000 Sellers (Worst Case)

For n = 100,000 sellers with nearly sorted data and first-element pivot:

**Worst-case comparisons** = n(n-1)/2 = 100,000 × 99,999 / 2 ≈ **5 × 10⁹ comparisons**

At a rate of ~10⁹ operations/second on modern hardware, this takes approximately **5 seconds** — completely unacceptable for a real-time leaderboard during a flash sale where updates must happen in milliseconds.

### 4.6 Why the Leaderboard Freezes During Sale Events

During a flash sale:
1. Sellers receive rapid score updates, so the leaderboard frequently needs re-sorting.
2. After each small batch of updates, the array is **nearly sorted** (most sellers' positions haven't changed much).
3. The first-element pivot in this nearly sorted input consistently picks the minimum or near-minimum element, creating maximally unbalanced partitions.
4. This triggers the O(n²) worst case, causing each sort operation to take several seconds instead of milliseconds.
5. With thousands of updates per minute during a sale, the system falls further and further behind, effectively freezing the leaderboard.

### 4.7 Improved Pivot Strategy

#### Option 1: Randomized Pivot

```
RANDOMIZED-PARTITION(A, low, high):
    r = RANDOM(low, high)       // Choose random index
    swap(A[r], A[high])         // Swap to end
    return PARTITION(A, low, high)
```

**How it helps:** With a randomly chosen pivot, the probability that every recursive call picks the worst possible pivot (minimum or maximum) becomes exponentially small. The expected time complexity is **Θ(n log n)** regardless of input order.

**Limitation:** Still has an O(n²) worst case with probability 1/n! — vanishingly unlikely but possible. Also introduces slight randomness overhead (random number generation per call).

#### Option 2: Median-of-Three Pivot

```
MEDIAN-OF-THREE(A, low, high):
    mid = (low + high) / 2
    // Sort A[low], A[mid], A[high] and return median
    if A[low] > A[mid]: swap(A[low], A[mid])
    if A[low] > A[high]: swap(A[low], A[high])
    if A[mid] > A[high]: swap(A[mid], A[high])
    // A[mid] is now the median
    swap(A[mid], A[high-1])    // Place median at high-1 for partitioning
    return A[high-1]
```

**How it helps:** By picking the median of the first, middle, and last elements, the pivot is guaranteed to be better than a purely random choice on structured inputs. It essentially eliminates worst-case behaviour on sorted, reverse-sorted, and "nearly sorted" arrays — which are exactly the common cases during leaderboard updates.

**Limitation:** Adds 3 comparisons and potentially 2 swaps per partition step — negligible overhead. Does not help if the data contains many identical values.

#### 4.7.1 Three-Way Partitioning for Equal Scores

During a flash sale, many sellers may have identical scores (e.g., multiple sellers at exactly 100 points). Standard two-way Quick Sort places all equal elements in one partition, forcing them to be re-partitioned repeatedly.

**Three-way partitioning (Dutch National Flag)** divides the array into three sections:
- **Left:** elements < pivot
- **Middle:** elements = pivot (all equal elements are placed in final position in one pass)
- **Right:** elements > pivot

```
THREE-WAY-PARTITION(A, low, high):
    pivot = A[low]
    lt = low        // A[low..lt-1] < pivot
    gt = high       // A[gt+1..high] > pivot
    i = low + 1     // Current element
    
    while i <= gt:
        if A[i] < pivot:
            swap(A[lt], A[i])
            lt++; i++
        else if A[i] > pivot:
            swap(A[i], A[gt])
            gt--
        else:
            i++                 // Equal to pivot, skip
    // A[lt..gt] all equal to pivot — no further recursion needed for this region
```

**Benefit for KartIQ:** When many sellers share the same score, three-way partitioning processes all of them in a single pass and excludes them from further recursion. This converts the O(n²) behaviour on many equal keys to **O(n log k)** where k is the number of distinct scores (k << n during events with tied scores).

### 4.8 Improved Quick Sort Pseudocode

```
QUICKSORT-IMPROVED(A, low, high):
    if low < high:
        // Use Median-of-Three pivot selection
        pivot_idx = MEDIAN-OF-THREE-INDEX(A, low, high)
        swap(A[pivot_idx], A[high])    // Place pivot at end
        
        // Three-way partition for equal scores
        lt, gt = THREE-WAY-PARTITION-INDICES(A, low, high)
        
        QUICKSORT-IMPROVED(A, low, lt - 1)    // Recurse on less-than region
        QUICKSORT-IMPROVED(A, gt + 1, high)   // Recurse on greater-than region
        // No recursion on equal region — it's already final!

MEDIAN-OF-THREE-INDEX(A, low, high):
    mid = (low + high) / 2
    if A[low] > A[mid]: swap(A[low], A[mid])
    if A[low] > A[high]: swap(A[low], A[high])
    if A[mid] > A[high]: swap(A[mid], A[high])
    return mid    // A[mid] is median
```

---

## 5. QUESTION (d) – MODULE 3: BINARY SEARCH – ORDER LOOKUP

### 5.1 Why Binary Search Requires Sorted Data

Binary Search works by repeatedly halving the search space. At each step, it compares the target with the middle element:
- If equal → found.
- If target < middle → search left half.
- If target > middle → search right half.

This strategy is **only valid when the data is sorted.** If the array is unsorted, the conclusion "target is not in the right half" would be wrong — the target might be anywhere. The correctness of Binary Search is entirely predicated on the sorted order invariant.

### 5.2 How Module 1's Output Provides the Precondition

Module 1 (Merge Sort) produces a fully sorted array of orders by timestamp each night. This sorted array is exactly the precondition that Module 3 (Binary Search) requires. This is a direct **data-flow dependency** between modules:

```
Module 1 (Merge Sort) → sorted array → Module 3 (Binary Search)
```

Without Module 1's output, Binary Search in Module 3 would not function correctly. This is an example of how the four modules form an integrated pipeline rather than independent components.

### 5.3 Divide-and-Conquer Search Process

Binary Search follows the divide-and-conquer paradigm:
- **Divide:** Compare target with mid element; eliminate half the array.
- **Conquer:** Recursively search the remaining half.
- **Combine:** No combine step needed — the base case directly returns the result.

### 5.4 Step-by-Step Search Example

**Sorted array (from Module 1 output):**
```
Index:  0        1        2        3        4        5
Data: (101,O4) (102,O2) (102,O5) (103,O6) (105,O1) (105,O3)
```

**Search target:** timestamp = 105

| Step | low | high | mid | A[mid].timestamp | Comparison | Action |
|------|-----|------|-----|-----------------|------------|--------|
| 1 | 0 | 5 | 2 | 102 | 105 > 102 | Search right half |
| 2 | 3 | 5 | 4 | 105 | 105 = 105 | **Found at index 4** |

**Result:** Order found at index 4 → (105, O1).

### 5.5 Handling Duplicate Timestamps – First-Occurrence Binary Search

**Problem:** Timestamps 105 appear at both index 4 (O1) and index 5 (O3). Standard Binary Search may return index 4 or 5 depending on where it happens to land. Customer support needs the **earliest** order with that timestamp.

**Solution – Lower-Bound Binary Search:**

Instead of stopping when we find a match, we continue searching **left** to find the first occurrence.

```
BINARY-SEARCH-FIRST(A, low, high, target):
    result = -1                      // Initialize: not found
    while low <= high:
        mid = (low + high) / 2
        
        if A[mid].timestamp == target:
            result = mid             // Record this match
            high = mid - 1          // Keep searching LEFT for earlier occurrence
        else if A[mid].timestamp < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return result                    // Returns index of FIRST occurrence, or -1
```

**Trace with duplicate example:**

**Sorted array:**
```
Index:  0        1        2        3        4        5
Data: (101,O4) (102,O2) (102,O5) (103,O6) (105,O1) (105,O3)
```

**Search target:** timestamp = 102

| Step | low | high | mid | A[mid] | Action | result |
|------|-----|------|-----|--------|--------|--------|
| 1 | 0 | 5 | 2 | (102,O5) | Match! Record result=2; search left → high=1 | 2 |
| 2 | 0 | 1 | 0 | (101,O4) | 101 < 102 → low=1 | 2 |
| 3 | 1 | 1 | 1 | (102,O2) | Match! Record result=1; search left → high=0 | 1 |
| 4 | 1 | 0 | — | low > high | Loop ends | 1 |

**Result:** Returns index 1 → **(102, O2)** — the first occurrence ✅  
O2 appears before O5 because Merge Sort preserved their arrival order (stability).

### 5.6 Mathematical Analysis

#### 5.6.1 Recurrence Formulation

```
T(n) = T(n/2) + Θ(1),    T(1) = Θ(1)
```

One recursive call on half the array, plus O(1) work per step (one comparison and one index update).

#### 5.6.2 Solution via Master Theorem

- a = 1 (one recursive call)
- b = 2 (halves the input)
- f(n) = Θ(1) = Θ(n^0)
- n^(log_b a) = n^(log₂ 1) = n^0 = 1

Since f(n) = Θ(n^(log₂ 1)) = Θ(1), we apply **Case 2:**
```
T(n) = Θ(log₂ n)
```

#### 5.6.3 Maximum Comparisons for 10,000,000 Orders

Maximum comparisons = ⌊log₂(10,000,000)⌋ + 1

log₂(10,000,000) = log₂(10^7) = 7 × log₂(10) ≈ 7 × 3.3219 ≈ **23.25**

Maximum comparisons = ⌊23.25⌋ + 1 = **24 comparisons**

For 10 million orders, Binary Search needs at most **24 comparisons** to locate any order. Compare this with linear search which would need up to 10,000,000 comparisons — a speedup factor of approximately **416,666×**.

### 5.7 Ordinary vs Lower-Bound Binary Search

| Aspect | Ordinary Binary Search | Lower-Bound Binary Search |
|--------|----------------------|--------------------------|
| **Stops when** | First match found | After entire search space eliminated |
| **Returns** | Any matching index | Index of **first** matching element |
| **Comparisons** | ≤ log₂(n) | ≤ log₂(n) + 1 (same asymptotic) |
| **Use case for KartIQ** | Checking existence of an order | Finding first order with given timestamp for audit trail |
| **Handles duplicates** | May return any duplicate | Always returns leftmost duplicate |

### 5.8 Pseudocode

**Standard Iterative Binary Search:**
```
BINARY-SEARCH(A, n, target):
    low = 0
    high = n - 1
    
    while low <= high:
        mid = (low + high) / 2       // Integer division
        
        if A[mid].timestamp == target:
            return mid               // Found
        else if A[mid].timestamp < target:
            low = mid + 1            // Search right half
        else:
            high = mid - 1           // Search left half
    
    return -1                        // Not found
```

**First-Occurrence (Lower-Bound) Binary Search:**
```
BINARY-SEARCH-LOWER-BOUND(A, n, target):
    low = 0
    high = n - 1
    result = -1
    
    while low <= high:
        mid = (low + high) / 2
        
        if A[mid].timestamp == target:
            result = mid             // Record match
            high = mid - 1          // Continue searching LEFT
        else if A[mid].timestamp < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return result                    // First occurrence index, or -1
```

---

## 6. QUESTION (e) – MODULE 4: STRASSEN'S MATRIX MULTIPLICATION – RECOMMENDATION SCORES

### 6.1 Why Conventional Matrix Multiplication Is Expensive

For two n×n matrices, conventional multiplication computes each of the n² result elements as a dot product of a row and a column, requiring n multiplications. Total:

**Scalar multiplications = n³**  
**Scalar additions = n²(n-1) ≈ n³**

The recurrence is:
```
T(n) = 8T(n/2) + Θ(n²)
```

By Master Theorem: n^(log₂ 8) = n³, f(n) = Θ(n²) < n³ → **Case 1 → T(n) = Θ(n³)**

For KartIQ's recommendation engine, matrices may be of size 1,000×1,000 or larger (item-feature and user-item matrices). At n=1,024: conventional requires 1,024³ ≈ **1.07 × 10⁹ multiplications** — pushing the limits of real-time response.

### 6.2 Strassen's Algorithm

Strassen (1969) observed that two 2×2 matrices can be multiplied using only **7 scalar multiplications** (instead of 8), at the cost of additional additions and subtractions.

For matrices A = [[a, b], [c, d]] and B = [[e, f], [g, h]]:

The seven products are defined as:

| Product | Formula |
|---------|---------|
| P₁ | (a + d)(e + h) |
| P₂ | (c + d)e |
| P₃ | a(f − h) |
| P₄ | d(g − e) |
| P₅ | (a + b)h |
| P₆ | (c − a)(e + f) |
| P₇ | (b − d)(g + h) |

The result matrix C = A × B is reconstructed as:

| Element | Formula |
|---------|---------|
| C₁₁ | P₁ + P₄ − P₅ + P₇ |
| C₁₂ | P₃ + P₅ |
| C₂₁ | P₂ + P₄ |
| C₂₂ | P₁ − P₂ + P₃ + P₆ |

### 6.3 Step-by-Step Calculation – Sample Matrices

Given:
```
A = [[1, 7],    B = [[1, 3],
     [3, 5]]         [7, 5]]
```

Identify elements: a=1, b=7, c=3, d=5, e=1, f=3, g=7, h=5

**Calculate all seven products:**

| Product | Substitution | Calculation | Value |
|---------|-------------|-------------|-------|
| P₁ | (a+d)(e+h) | (1+5)(1+5) | 6×6 = **36** |
| P₂ | (c+d)e | (3+5)×1 | 8×1 = **8** |
| P₃ | a(f−h) | 1×(3−5) | 1×(−2) = **−2** |
| P₄ | d(g−e) | 5×(7−1) | 5×6 = **30** |
| P₅ | (a+b)h | (1+7)×5 | 8×5 = **40** |
| P₆ | (c−a)(e+f) | (3−1)(1+3) | 2×4 = **8** |
| P₇ | (b−d)(g+h) | (7−5)(7+5) | 2×12 = **24** |

**Reconstruction:**

| Element | Formula | Substitution | Value |
|---------|---------|-------------|-------|
| C₁₁ | P₁+P₄−P₅+P₇ | 36+30−40+24 | **50** |
| C₁₂ | P₃+P₅ | −2+40 | **38** |
| C₂₁ | P₂+P₄ | 8+30 | **38** |
| C₂₂ | P₁−P₂+P₃+P₆ | 36−8+(−2)+8 | **34** |

**Strassen Result:**
```
C = [[50, 38],
     [38, 34]]
```

### 6.4 Verification by Conventional Multiplication

```
C₁₁ = (1×1) + (7×7) = 1 + 49 = 50  ✅
C₁₂ = (1×3) + (7×5) = 3 + 35 = 38  ✅
C₂₁ = (3×1) + (5×7) = 3 + 35 = 38  ✅
C₂₂ = (3×3) + (5×5) = 9 + 25 = 34  ✅
```

**Both methods produce the same result. Strassen's algorithm is verified correct. ✅**

### 6.5 Mathematical Analysis

#### 6.5.1 Conventional Recurrence

```
T(n) = 8T(n/2) + Θ(n²)
```

By Master Theorem: a=8, b=2, f(n)=Θ(n²)  
n^(log₂ 8) = n^3  
f(n) = Θ(n²) = O(n^(3−ε)) for ε=1 → **Case 1:**

```
T(n) = Θ(n³)
```

#### 6.5.2 Strassen Recurrence

```
T(n) = 7T(n/2) + Θ(n²)
```

By Master Theorem: a=7, b=2, f(n)=Θ(n²)  
n^(log₂ 7) ≈ n^2.807  
f(n) = Θ(n²) = O(n^(2.807−ε)) for small ε → **Case 1:**

```
T(n) = Θ(n^(log₂ 7)) ≈ Θ(n^2.807)
```

#### 6.5.3 Scalar Multiplication Count for n = 1,024

For n = 1,024 = 2^10:

**Conventional method:**
- Multiplications = n³ = 1,024³ = 2^30 ≈ **1,073,741,824** (≈ 1.07 × 10⁹)

**Strassen's method:**
- Multiplications = 7^(log₂ n) = 7^10

Computing 7^10:
- 7^1 = 7
- 7^2 = 49
- 7^4 = 49² = 2,401
- 7^8 = 2,401² = 5,764,801
- 7^10 = 7^8 × 7^2 = 5,764,801 × 49 = **282,475,249** (≈ 2.82 × 10⁸)

**Comparison:**

| Method | Scalar Multiplications (n=1,024) | Reduction |
|--------|----------------------------------|-----------|
| Conventional | 1,073,741,824 | — |
| Strassen | 282,475,249 | ≈ **73.7% fewer** multiplications |
| Ratio | — | Conventional requires ≈ **3.8× more** multiplications |

Strassen's algorithm requires approximately **3.8 times fewer** scalar multiplications than conventional multiplication for 1,024×1,024 matrices.

### 6.6 Practical Discussion

#### 6.6.1 Why Strassen May Not Always Be Faster in Practice

Despite the theoretical advantage, Strassen has real-world limitations:

| Factor | Explanation |
|--------|------------|
| **Additional additions/subtractions** | Strassen requires 18 matrix additions/subtractions per level vs 4 for conventional. For small matrices, this overhead dominates. |
| **Recursion overhead** | Function call overhead accumulates over log₂(n) recursion levels. |
| **Memory usage** | Strassen requires O(n² log n) auxiliary space — significantly more than conventional O(n²) for the output. Excessive memory use causes cache thrashing. |
| **Numerical precision** | The additional additions introduce more floating-point rounding errors, which matters for scientific computation (less critical for KartIQ's recommendation scores). |
| **Matrix padding** | Strassen requires square matrices with power-of-2 dimensions. Non-square matrices must be padded with zeros, wasting computation. |

#### 6.6.2 Hybrid Strassen Algorithm

The standard solution is a **hybrid algorithm** that uses Strassen for large subproblems and switches to conventional multiplication below a threshold size n₀:

```
HYBRID-STRASSEN(A, B, n):
    if n <= THRESHOLD:               // e.g., THRESHOLD = 64 or 128
        return CONVENTIONAL-MULTIPLY(A, B, n)
    
    // Divide into four n/2 × n/2 submatrices
    A11, A12, A21, A22 = SPLIT(A)
    B11, B12, B21, B22 = SPLIT(B)
    
    // Compute 7 Strassen products (each is a recursive call)
    P1 = HYBRID-STRASSEN(A11+A22, B11+B22, n/2)
    P2 = HYBRID-STRASSEN(A21+A22, B11,     n/2)
    P3 = HYBRID-STRASSEN(A11,     B12-B22, n/2)
    P4 = HYBRID-STRASSEN(A22,     B21-B11, n/2)
    P5 = HYBRID-STRASSEN(A11+A12, B22,     n/2)
    P6 = HYBRID-STRASSEN(A21-A11, B11+B12, n/2)
    P7 = HYBRID-STRASSEN(A12-A22, B21+B22, n/2)
    
    // Reconstruct result
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6
    
    return COMBINE(C11, C12, C21, C22)

CONVENTIONAL-MULTIPLY(A, B, n):
    C = zero matrix of size n×n
    for i = 0 to n-1:
        for j = 0 to n-1:
            for k = 0 to n-1:
                C[i][j] += A[i][k] × B[k][j]
    return C
```

**Justification for Hybrid Approach:**
- For small n (≤ 64), conventional multiplication is faster due to lower overhead and better cache locality.
- For large n (> 64), Strassen's sublinear exponent (2.807 vs 3) provides meaningful speedup.
- The threshold (typically 32–128) is tuned empirically based on the specific hardware and matrix structure.
- This approach gives the best of both worlds: asymptotic efficiency at scale, with practical efficiency for small subproblems.

---

## 7. QUESTION (f) – FINAL SYSTEM DESIGN AND JUSTIFICATION

### 7.1 Final System Architecture Comparison Table

| **Module** | **Selected Algorithm** | **Time Complexity** | **Auxiliary Space** | **Reason for Selection** | **Main Trade-off** | **Change Condition** |
|---|---|---|---|---|---|---|
| **1. Nightly Order Consolidation** | Stable Merge Sort | Θ(n log n) always | O(n) | Only stable divide-and-conquer sort guaranteeing O(n log n) in all cases; audit-compliant stability for equal timestamps | Requires O(n) extra memory — costly for 10M+ records; not in-place | Switch to external Merge Sort if data exceeds RAM; consider Tim Sort if near-sorted input is common (exploits existing runs) |
| **2. Live Seller Leaderboard** | Quick Sort with Median-of-Three + Three-Way Partitioning | Θ(n log n) average/expected | O(log n) stack | In-place sorting; optimal average case; three-way partitioning efficiently handles equal scores during sale events | Worst case still O(n²) if pivot selection fails; not stable (acceptable since seller IDs are unique) | Switch to Merge Sort if strict ordering guarantees required or if input is provably nearly sorted; switch to Heap Sort for guaranteed O(n log n) in all cases |
| **3. Order Lookup** | Lower-Bound Binary Search | Θ(log n) | O(1) | Requires pre-sorted input (provided by Module 1); returns first occurrence of duplicate timestamp for audit trail; maximum 24 comparisons for 10M records | Completely dependent on Module 1's sorted output; cannot function on unsorted data | Switch to hash-table lookup O(1) if order IDs (not timestamps) are the primary search key and duplicates are not an issue |
| **4. Recommendation Scores** | Hybrid Strassen Matrix Multiplication | O(n^2.807) for large n; O(n³) for small n (threshold) | O(n² log n) | Reduces scalar multiplications by ~74% for large matrices; practical hybrid approach avoids overhead for small submatrices | Higher implementation complexity; additional memory usage; numerical precision slightly lower than conventional | Revert to conventional O(n³) for matrices smaller than threshold (~64×64); use specialised sparse matrix algorithms if matrices are sparse (>80% zeros) |

### 7.2 How the Four Modules Work Together as an Integrated Platform

The four modules do not operate in isolation — they form a coherent pipeline where each module's output either feeds directly into or enables the next:

```
┌─────────────────────────────────────────────────────────┐
│              KartIQ Data Analytics Pipeline              │
└─────────────────────────────────────────────────────────┘

Regional Databases (Order Data)
        │
        ▼
┌───────────────────┐    Nightly Batch
│   MODULE 1        │    ─────────────
│   Stable          │    Sorts ~10M orders by timestamp
│   Merge Sort      │    Produces: sorted_orders[]
└───────┬───────────┘    Complexity: Θ(n log n), stable
        │
        │  sorted_orders[]
        ▼
┌───────────────────┐    On Demand
│   MODULE 3        │    ─────────
│   Lower-Bound     │    Looks up any order in ≤24 steps
│   Binary Search   │    Uses: sorted_orders[] from Module 1
└───────────────────┘    Complexity: Θ(log n)

Seller Score Updates (Real-Time Stream)
        │
        ▼
┌───────────────────┐    Real-Time (per flash sale)
│   MODULE 2        │    ───────────────────────────
│   Quick Sort      │    Sorts ~100K seller scores
│   (Improved)      │    Produces: ranked_sellers[]
└───────────────────┘    Complexity: Θ(n log n) average

User Interaction Matrices
        │
        ▼
┌───────────────────┐    Periodic Batch
│   MODULE 4        │    ─────────────
│   Hybrid          │    Computes recommendation matrices
│   Strassen        │    Produces: recommendation_scores[]
└───────────────────┘    Complexity: O(n^2.807)
        │
        ▼
Personalised Product Recommendations → Users
```

**Integration Details:**

1. **Module 1 → Module 3 (Direct Data Flow):**  
   Module 1's sorted output is the **precondition** for Module 3. Without the nightly sort, Binary Search would not function. This dependency means Module 1 must complete its nightly batch before the customer support team's lookup service comes online each morning.

2. **Module 2 (Independent Real-Time):**  
   The seller leaderboard operates independently of Modules 1 and 3. It processes a continuous stream of seller score updates during operating hours. Its output (ranked_sellers[]) feeds the leaderboard display on the platform frontend.

3. **Module 4 (Periodic Recommendation Batch):**  
   Strassen's multiplication processes the user–item interaction matrix and item–feature matrix to produce recommendation scores. These are recomputed periodically (e.g., hourly or daily) and stored for real-time access when users browse the platform.

4. **System-Level Guarantees:**
   - Audit compliance: Provided by Module 1 (stability) and Module 3 (first-occurrence search).
   - Real-time performance: Provided by Module 2 (fast in-place sort) and Module 3 (logarithmic lookup).
   - Scalability: All four algorithms scale gracefully — none degrades to O(n²) or O(n³) under normal operating conditions with proper configuration.

---

## 8. OVERALL CONCLUSION

This case study has demonstrated how the **Divide-and-Conquer paradigm** provides elegant and efficient solutions to four distinct computational challenges in KartIQ's retail analytics platform:

| Module | Problem | Algorithm | Key Takeaway |
|--------|---------|-----------|-------------|
| Order Consolidation | Stable sorting of 10M records | Merge Sort | Stability is a property of the combine step; Θ(n log n) guaranteed |
| Seller Leaderboard | Real-time sorting of 100K records | Quick Sort (Improved) | Pivot selection is the difference between O(n log n) and O(n²) |
| Order Lookup | Finding records in 10M sorted entries | Binary Search | log₂(10M) ≈ 24 comparisons — Divide and Conquer at its purest |
| Recommendation Scores | Large matrix multiplication | Hybrid Strassen | Reducing recursive calls from 8 to 7 cuts complexity from n³ to n^2.807 |

The common thread across all four modules is **problem decomposition**: by breaking large problems into smaller, identical subproblems, divide-and-conquer algorithms achieve time complexities that make large-scale real-time platforms feasible. The 232 million comparisons for Merge Sort, 24 comparisons for Binary Search, and 282 million scalar multiplications (versus 1 billion for conventional) for Strassen are not just numbers — they represent the difference between a system that works and one that freezes under load.

The critical insight from this study is that **algorithm selection is not complete without configuration selection.** Quick Sort is fast — but only with the right pivot strategy. Strassen is efficient — but only above a certain matrix size. Merge Sort is stable — but its O(n) memory requirement must be planned for. A deep understanding of both the theoretical properties and practical constraints of each algorithm is essential for building production-grade systems.

---

## 9. REFERENCES

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.

2. Strassen, V. (1969). Gaussian elimination is not optimal. *Numerische Mathematik*, 13(4), 354–356.

3. Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley.

4. Knuth, D. E. (1998). *The Art of Computer Programming, Volume 3: Sorting and Searching* (2nd ed.). Addison-Wesley.

5. Hoare, C. A. R. (1962). Quicksort. *The Computer Journal*, 5(1), 10–16.

6. Bentley, J. L., & McIlroy, M. D. (1993). Engineering a sort function. *Software: Practice and Experience*, 23(11), 1249–1265.

---

## 10. STUDENT DECLARATION

I hereby declare that:

1. This case study assignment is my own independent work.
2. All sources consulted have been properly cited in the References section.
3. I have not submitted this work, or any part of it, for assessment in any other course.
4. I understand that academic dishonesty is a serious violation of university regulations.
5. All mathematical calculations and algorithm traces have been verified by me personally.

---

**Student Name:** M.Gnanesh kumar naidu

**Registration Number:** 192371051

**Course:** Design and Analysis of Algorithms (CSA0607)

**Assessment:** CO3 – Case Study

**Signature:** ______________________

**Date:** 15-11-2026

---

*Department of Computer Science and Engineering*  
*Velammal College of Engineering and Technology*

---

> **End of Assignment**

