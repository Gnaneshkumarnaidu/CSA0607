# Q3 – Breaking the Quadratic Barrier: Karatsuba Multiplication (7 Marks)

### Shared Group Work
Implemented standard $O(n^2)$ digit-by-digit multiplication and Karatsuba's divide-and-conquer algorithm.

### Student A – Algorithmic Derivation (M.Gnanesh kumar naidu)
- **Integer Decomposition:** Let $X = X_H \cdot 10^m + X_L$ and $Y = Y_H \cdot 10^m + Y_L$, where $m = \lceil n/2 
ceil$.
  Product $XY = X_H Y_H \cdot 10^{2m} + (X_H Y_L + X_L Y_H) \cdot 10^m + X_L Y_L$.
  Standard approach requires 4 multiplications: $X_H Y_H, X_H Y_L, X_L Y_H, X_L Y_L$.
- **Karatsuba's Algebraic Reduction:**
  $Z_2 = X_H Y_H$
  $Z_0 = X_L Y_L$
  $Z_1 = (X_H + X_L)(Y_H + Y_L) - Z_2 - Z_0 = X_H Y_L + X_L Y_H$
  This requires only 3 multiplications instead of 4.
- **Recurrence & Solution:**
  $$T(n) = 3T(n/2) + \Theta(n)$$
  By Master Theorem ($a=3, b=2$): $\log_2 3 pprox 1.585 > 1$.
  $$T(n) = \Theta(n^{\log_2 3}) pprox \Theta(n^{1.585})$$

### Student B – Crossover Investigation (Shaik Mohammad Sohan)
- **Experimental Operations:**
  For 16-digit integers:
  Standard multiplication: $16 	imes 16 = 256$ single-digit operations.
  Karatsuba recursive calls: 81 calls ($3^4 = 81$).
- **Crossover Point:** Due to addition, subtraction, and call-stack overheads, the practical runtime crossover occurs around 32 to 64 digits (or words). Below this threshold, grade-school multiplication is faster.

### Joint Conclusion
**Answer:** Superior asymptotic complexity dominates only as $n 	o \infty$. When constant factors and additive overheads exceed the computational savings of fewer multiplications, asymptotic superiority does not translate into better performance on small inputs.
