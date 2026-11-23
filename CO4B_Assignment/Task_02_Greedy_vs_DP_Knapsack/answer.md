# TASK 2 – GREEDY vs DYNAMIC PROGRAMMING: Build It, Break It, Explain It (9 Marks)

### 2.1 Normal Case (2 Marks)
- **Instance:** Vehicle Capacity = 50. Items: A(w=10, v=60, dens=6.0), B(w=20, v=100, dens=5.0), C(w=30, v=120, dens=4.0).
- **Decision Sequence:** Greedy by density selects A completely (10kg, 60 val), then B completely (20kg, 100 val), then 2/3 of C (20kg, 80 val). Total Fractional Value = 240.0.
- For 0/1 knapsack, taking A and B gives 30kg, leaving 20kg which cannot fit C. DP tests all combinations and takes A and C (40kg, 180 val) or B and C (50kg, 220 val).

### 2.2 Break the Greedy Intuition (3 Marks)
- **Adversarial 0/1 Counterexample:** Capacity $W = 40$.
  - Item 1: Weight = 10, Value = 60 (Density = 6.0)
  - Item 2: Weight = 20, Value = 100 (Density = 5.0)
  - Item 3: Weight = 20, Value = 100 (Density = 5.0)
- **Greedy Commitment Trap:** Greedy sorts by density and immediately commits to Item 1 (10kg, 60). Remaining capacity is $40 - 10 = 30$kg. It then takes Item 2 (20kg, 100). Remaining capacity is 10kg, leaving Item 3 stranded! Greedy total value $= 160$.
- **DP Global Optimum:** DP recognizes that skipping the locally highest-density Item 1 allows selecting both Item 2 and Item 3, filling the vehicle perfectly: $20 + 20 = 40$kg for a total value of **200**!
- **First Greedy Commitment:** The irrevocable choice of Item 1 locks out the global optimum.

### 2.3 Engineering Comparison (2 Marks)
| Metric | Fractional Knapsack (Greedy) | 0/1 Knapsack (Dynamic Programming) |
|---|---|---|
| Computational Work | $O(n \log n)$ (sorting items) | $O(n \cdot W)$ (pseudo-polynomial) |
| Memory Requirement | $O(1)$ auxiliary (in-place sort) | $O(n \cdot W)$ or $O(W)$ memory table |
| Solution Quality | Mathematically optimal for divisible items | Mathematically optimal for indivisible items |
| Optimality Guarantee | Guaranteed for fractional, FAILS for 0/1 | Strictly guaranteed globally optimal |

### 2.4 Changed Requirement: Extremely Fast Decision (2 Marks)
If management mandates immediate decisions within milliseconds for high throughput, greedy heuristic is selected. The fractional relaxation or greedy 0/1 heuristic runs in $O(n \log n)$ time, delivering at least a $1/2$-approximation guaranteed bound with minimal CPU and zero memory overhead.
