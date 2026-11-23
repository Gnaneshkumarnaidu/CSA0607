# Q4 – Strassen's Matrix Multiplication (7 Marks)

### Shared Group Work
Study block matrix multiplication and implement both conventional $O(n^3)$ and Strassen's $O(n^{\log_2 7})$ methods.

### Student B – Algebraic Design & Correctness (Shaik Mohammad Sohan)
- **Block Decomposition:** Partition matrices $A$ and $B$ into four $(n/2) 	imes (n/2)$ submatrices.
- **Eight Standard Multiplications:**
  $C_{11} = A_{11}B_{11} + A_{12}B_{21}$, $C_{12} = A_{11}B_{12} + A_{12}B_{22}$, etc.
- **Strassen's 7 Products:**
  $M_1 = (A_{11} + A_{22})(B_{11} + B_{22})$
  $M_2 = (A_{21} + A_{22})B_{11}$
  $M_3 = A_{11}(B_{12} - B_{22})$
  $M_4 = A_{22}(B_{21} - B_{11})$
  $M_5 = (A_{11} + A_{12})B_{22}$
  $M_6 = (A_{21} - A_{11})(B_{11} + B_{12})$
  $M_7 = (A_{12} - A_{22})(B_{21} + B_{22})$
- **Reconstruction:**
  $C_{11} = M_1 + M_4 - M_5 + M_7 = A_{11}B_{11} + A_{12}B_{21}$ (Algebraically exact).

### Student A – Experimental & Engineering Analysis (M.Gnanesh kumar naidu)
- **4x4 Matrix Multiplication Counts:**
  Standard algorithm: $n^3 = 4^3 = 64$ multiplications.
  Strassen algorithm: $7^{\log_2 4} = 7^2 = 49$ multiplications (23.4% reduction).
- **Overhead Analysis:** Strassen requires 18 matrix additions/subtractions per recursive level, non-contiguous memory allocations, and cache penalties.

### Joint Engineering Decision
**Conditions for Conventional Multiplication:** Conventional multiplication is preferred when:
1. Matrix dimensions are below crossover ($n < 64$ or $128$).
2. Memory is highly constrained (Strassen requires substantial auxiliary memory).
3. Numerical stability is vital (Strassen introduces higher accumulated round-off errors).
