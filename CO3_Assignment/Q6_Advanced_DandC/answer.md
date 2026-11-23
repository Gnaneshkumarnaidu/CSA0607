# Q6 – Advanced Divide-and-Conquer Mini-Investigations (7 Marks)

### Student A – Median of Medians (M.Gnanesh kumar naidu)
- **Grouping:** Elements partitioned into $\lfloor n/5 
floor$ groups of 5.
- **Pivot Selection:** Compute median of each 5-element group, then recursively find the median of these medians.
- **Guarantee:** At least $3 	imes (\lceil rac{1}{2} \lceil rac{n}{5} 
ceil 
ceil) pprox rac{3n}{10}$ elements are strictly smaller and $rac{3n}{10}$ larger.
- **Worst-Case Bound:**
  $$T(n) \le T(n/5) + T(7n/10) + \Theta(n) \implies T(n) = \Theta(n)$$
  Guarantees deterministic $O(n)$ selection.

### Student B – Meet-in-the-Middle (Shaik Mohammad Sohan)
- **Subset Sum Decomposition:** Array of $n$ elements split into two equal halves of size $n/2$.
- **Space Reduction:** Generate $2^{n/2}$ sums for each half. Sort second half and binary search for $Target - s_1$.
- **Complexity:** Reduced from $O(2^n)$ to $O(2^{n/2} \log(2^{n/2})) = O(n \cdot 2^{n/2})$.
- **Trade-off:** Achieves massive time reduction by using $O(2^{n/2})$ auxiliary memory.
