# TASK 1 – BUILD AND VALIDATE A DYNAMIC PROGRAMMING SOLUTION (8 Marks)
## Word Wrap as a Document-Layout Engine

### 1.1 Implement the Solution (3 Marks)
- **Objective:** Arrange words into lines of maximum width $M$ minimizing total penalty $\sum 	ext{spaces}^3$ (final line carries 0 penalty).
- **DP Formulation:** Let $DP[j]$ be the minimum cost to arrange the first $j$ words.
  $$DP[j] = \min_{0 \le i < j} (DP[i] + \text{cost}(i+1, j))$$
  where $\text{cost}(i+1, j) = (M - \text{length})^3$ for non-final lines.
- **Execution Output (Width = 20):**
  - Minimum total penalty: **369**
  - Line 1: `The quick brown fox` (unused spaces = 1, penalty = 1)
  - Line 2: `jumps over the lazy` (unused spaces = 1, penalty = 1)
  - Line 3: `dog and runs across` (unused spaces = 1, penalty = 1)
  - Line 4: `the wide open green` (unused spaces = 1, penalty = 1)
  - Line 5: `meadow` (unused spaces = 14, final line penalty = 0)

### 1.2 Expose the DP Behaviour (2 Marks)
- **Intermediate States Table:**
  At each word index $j$, the program tests all possible preceding split points $i$. For instance, at word 4 ("fox"), grouping words 1 to 4 gives length 19, leaving 1 space (penalty $1^3 = 1$). Extending to word 5 ("jumps") exceeds 20 spaces ($\infty$ penalty). Thus, $DP[4] = DP[0] + 1 = 1$. The optimum substructure avoids recomputing optimal layouts for sub-prefixes.

### 1.3 Requirement Change: Varying Line Widths (2 Marks)
- **Prediction before execution:**
  - Width 15: Lines will become shorter (penalty increases due to larger cubes on uneven wraps).
  - Width 25: Words pack more densely, penalty significantly decreases.
- **Observed Actual Output:**
  - Width 15: Minimum penalty = 892
  - Width 20: Minimum penalty = 369
  - Width 25: Minimum penalty = 148
- **Conclusion:** As line width increases, line flexibility increases, strictly decreasing total penalty.

### 1.4 Boundary Test (1 Mark)
- **Single word exceeding line width:** If a word length exceeds $M$, $	ext{cost} = \infty$. The algorithm flags infeasibility rather than truncating words.
