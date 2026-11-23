# Q7 – Day-4 Design Challenge: Divide & Conquer from First Principles (10 Marks)

### Stage 1 – Independent Design Proposals
- **Student A Initial Proposal:** Divide array into equal halves. Maximum subarray either lies completely in left half, completely in right half, or spans across midpoint. Base case: single element returns itself.
- **Student B Initial Proposal:** Divide into halves, return prefix sums, suffix sums, and total sum to allow $O(1)$ combine step.

### Stage 2 – Compare the Two Designs
Both students agreed on the tripartite decomposition. Student B's proposal allows combining in $O(1)$ if 4-tuples are maintained, while Student A's linear crossing scan is simple and gives $O(n \log n)$. The team selected Student A's intuitive crossing scan for primary implementation and Student B's for constant-time combine analysis.

### Stage 3 – Joint Final Design & Pseudocode
```
ALGORITHM MaxSubarray(A, low, high)
  if low == high then
    return (A[low], low, high)
  mid = (low + high) / 2
  (left_sum, l_low, l_high) = MaxSubarray(A, low, mid)
  (right_sum, r_low, r_high) = MaxSubarray(A, mid + 1, high)
  (cross_sum, c_low, c_high) = MaxCrossingSubarray(A, low, mid, high)
  return max of (left_sum, right_sum, cross_sum)
```

### Stage 4 – Mathematical & Experimental Validation
- **Student A (Mathematical):** $T(n) = 2T(n/2) + \Theta(n)$. By Master Theorem ($a=2, b=2, d=1$), $T(n) = \Theta(n \log n)$.
- **Student B (Experimental):** Input `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`. Optimum subarray found: `[4, -1, 2, 1]` with sum $= 6$. Total operations $= 25$.

### Stage 5 – Cross-Defence
- **Student A:** Validated that Kadane's dynamic programming achieves $O(n)$, but D&C provides tree-level parallelism where independent partitions can be computed on separate processor cores.
- **Student B:** Formulated the recurrence from the exact recursive calls and linear midpoint scan.

### Contribution Record
| Question | Student A Contribution (M.Gnanesh kumar naidu) | Student B Contribution (S. M. Sohan) | Joint Work |
|---|---|---|---|
| Q1 | Mathematical derivation & Recurrence | Experimental setup & Elimination logic | Max/Min Tournament Strategy |
| Q2 | Quick Sort investigation & recursion tree | Merge Sort predictability analysis | Sorting component selection |
| Q3 | Algorithmic derivation of $O(n^{1.585})$ | Crossover point investigation | Overhead analysis |
| Q4 | Experimental matrix operations | Algebraic 7-product correctness | Engineering usage decision |
| Q5 | 2D Geometry decomposition & Strip design | Experimental distance counter & validation | Boundary 7-point geometry proof |
| Q6 | Median of Medians deterministic $O(n)$ | Meet-in-the-Middle subset sum | Selection vs search space trade-off |
| Q7 | Independent proposal & Recurrence solve | Independent proposal & Test implementation | Joint D&C architecture |
