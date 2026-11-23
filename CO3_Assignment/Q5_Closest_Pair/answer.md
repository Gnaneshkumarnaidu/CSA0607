# Q5 – Upgrading Closest Pair Using Divide and Conquer (6 Marks)

### Shared Group Work
Implemented $O(n^2)$ pairwise brute force and $O(n \log n)$ divide-and-conquer closest-pair algorithm.

### Student A – Decomposition Design (M.Gnanesh kumar naidu)
- **Organization:** Presort points by $X$-coordinate ($P_x$) and $Y$-coordinate ($P_y$).
- **Decomposition:** Divide by vertical line $x = x_{mid}$ into left half $Q$ and right half $R$.
- **Recursive Return:** $\delta = \min(\delta_L, \delta_R)$.
- **Combine Step & Strip:** Construct strip of points within distance $\delta$ from vertical dividing line. For each point in strip, only points within $\delta$ vertical distance need inspection (at most 7 subsequent points).

### Student B – Comparative Evidence (Shaik Mohammad Sohan)
- **Measured Operations ($n=10$):**
  Brute-force comparisons: $rac{10 	imes 9}{2} = 45$ distance calculations.
  D&C comparisons: 18 distance calculations.
- **Cross-Understanding:** The strip inspection only requires checking at most 7 neighbors because no two points in the same half can be closer than $\delta$, geometrically packing at most 8 points in a $\delta 	imes 2\delta$ rectangle.
