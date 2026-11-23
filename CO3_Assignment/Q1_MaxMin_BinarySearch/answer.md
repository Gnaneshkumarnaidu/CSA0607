# Q1 – Decomposition and Elimination in Ordered Data (6 Marks)

## Part A – Finding Maximum and Minimum (Tournament Divide & Conquer)

### Shared Group Work
- **Problem Formulation:** Given an unsorted array $A[0 \dots n-1]$ of $n$ elements, determine both the minimum and maximum values using optimal comparisons.
- **D&C / Tournament Strategy:** Recursively divide the array into two halves, compute the pair $(\min_1, \max_1)$ for the left half and $(\min_2, \max_2)$ for the right half, and combine them with two scalar comparisons: $\min = \min(\min_1, \min_2)$ and $\max = \max(\max_1, \max_2)$.
- **Base Cases:**
  - $n=1$: $\min = \max = A[low]$ (0 comparisons).
  - $n=2$: 1 comparison between $A[low]$ and $A[high]$ sets initial min and max.
- **Return Value:** A 2-tuple $(	ext{min\_val}, 	ext{max\_val})$.

### Student A – Design & Mathematical Analysis (M.Gnanesh kumar naidu)
- **Decomposition Tree:**
  At root $n=16$, split into $8$ and $8$. Each $8$ splits into $4$ and $4$, down to pairs of $2$.
- **Combine Operation:**
  For subproblems returning $(m_1, M_1)$ and $(m_2, M_2)$, combine using:
  $m = m_1 < m_2 \ ? \ m_1 : m_2$ (1 comparison)
  $M = M_1 > M_2 \ ? \ M_1 : M_2$ (1 comparison)
  Total combine cost = 2 comparisons per node.
- **Recurrence & Derivation:**
  $$T(n) = 2T(n/2) + 2 \quad 	ext{for } n > 2, \quad T(2) = 1, \ T(1) = 0$$
  For $n = 2^k$:
  $$T(n) = rac{3n}{2} - 2$$
- **Mathematical Comparison:**
  - Independent Linear Scan for Min and Max: $(n-1) + (n-1) = 2n - 2$ comparisons.
  - For $n=16$: Linear Scan $= 30$ comparisons. Tournament D&C $= 1.5(16) - 2 = 22$ comparisons.
  - Percentage reduction $= 26.7\%$.

### Student B – Experimental Validation (Shaik Mohammad Sohan)
- **Dataset:** Deterministic random 16-element array: `[24, 13, 88, 45, 12, 67, 91, 3, 55, 76, 42, 19, 8, 99, 31, 60]`.
- **Measured Comparisons:** Exactly 22 comparisons.
- **Discrepancy:** 0 discrepancy with the theoretical bound $1.5(16)-2 = 22$.

---

## Part B – Binary Search

### Shared Group Work
Derive search on sorted array eliminating half of the candidates per step.

### Student A – Experimental Investigation (M.Gnanesh kumar naidu)
- **Target Found (55):** Found at index 9, Comparisons = 3 ($\le \lfloor \log_2 16 
floor + 1 = 5$).
- **Target Not Found (50):** Terminated after 4 comparisons with status not found.

### Student B – Elimination Logic (Shaik Mohammad Sohan)
- **Decision Rule:** Compare target with $A[mid]$. If target $< A[mid]$, eliminate subarray $A[mid \dots high]$ because the array is monotonically sorted, ensuring all elements at or above $mid$ are strictly greater than target.
- **Termination:** When $low > high$ (search space empty) or target matches.
- **Efficiency:** Halving the remaining search space at every step yields logarithmic complexity $\Theta(\log n)$.
