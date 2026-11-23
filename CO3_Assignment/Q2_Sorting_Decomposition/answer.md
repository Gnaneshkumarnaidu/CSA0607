# Q2 – The Quality of Decomposition in Sorting (7 Marks)

### Shared Group Work
Implement Merge Sort and Lomuto-partition Quick Sort.

### Student A – Quick Sort Investigation (M.Gnanesh kumar naidu)
- **Balanced Input (Random):**
  $n=16$ random elements. Maximum recursion depth $= 5 pprox \lceil \log_2 16 
ceil + 1$. Total comparisons $= 45$.
- **Severely Unbalanced Input (Sorted Array):**
  $n=16$ strictly ascending array. Every partition isolates 1 element: subproblems of size $0$ and $n-1$.
  Maximum recursion depth $= 15 = n-1$. Total comparisons $= rac{16 	imes 15}{2} = 120$.
- **Pivot Influence:** Pivot selection directly governs the balance of the recursion tree. Fixed-endpoint pivots fail catastrophically on sorted or patterned inputs.

### Student B – Comparative D&C Analysis (Shaik Mohammad Sohan)
- **Merge Sort Decomposition:** Divides exactly at the static index midpoint $\lfloor n/2 
floor$, independent of values.
- **Recursion Tree Height:** Merge Sort tree is guaranteed height $\lceil \log_2 n 
ceil$. Quick Sort varies between $\log_2 n$ and $n$.
- **Predictability & Worst Case:** Merge Sort guarantees $\Theta(n \log n)$ time in all cases. Quick Sort degrades to $O(n^2)$ when splits are skewed $1 : n-1$.

### Joint Design Question
**Question:** If characteristics of input data are unknown in advance, what information is required before choosing between Merge Sort and Quick Sort?
**Answer:** We require:
1. Memory budget (Merge Sort requires $O(n)$ auxiliary space, while in-place Quick Sort requires $O(\log n)$ call-stack space).
2. Stability requirements (Merge Sort preserves original order of equal keys).
3. Worst-case latency guarantees (Critical systems require Merge Sort's deterministic $O(n \log n)$ ceiling rather than risking Quick Sort's $O(n^2)$ stall).
