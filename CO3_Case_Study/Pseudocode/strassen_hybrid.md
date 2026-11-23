# Hybrid Strassen Matrix Multiplication – Pseudocode
# Module 4: Recommendation Scores
# KartIQ – Retail Data Analytics Platform | CO3 Case Study

## Algorithm: Hybrid Strassen (Strassen above threshold, Conventional below)

### Time Complexity:  O(n^2.807) for large matrices; O(n³) below threshold
### Space Complexity: O(n² log n) — multiple intermediate matrix buffers


HYBRID-STRASSEN(A, B, n):
──────────────────────────
    if n <= THRESHOLD:                      // e.g., THRESHOLD = 64 or 128
        return CONVENTIONAL-MULTIPLY(A, B, n)
    
    if n is not a power of 2:
        n_padded ← next power of 2 ≥ n
        A ← PAD-WITH-ZEROS(A, n_padded)    // Pad to n_padded × n_padded
        B ← PAD-WITH-ZEROS(B, n_padded)
        C ← HYBRID-STRASSEN(A, B, n_padded)
        return C[0..n-1][0..n-1]           // Extract original-size submatrix

    half ← n / 2

    // Split A and B into four n/2 × n/2 submatrices
    A11, A12, A21, A22 ← SPLIT(A, half)
    B11, B12, B21, B22 ← SPLIT(B, half)

    // Compute 7 Strassen products (each is a recursive call)
    P1 ← HYBRID-STRASSEN(A11 + A22, B11 + B22, half)   // (a+d)(e+h)
    P2 ← HYBRID-STRASSEN(A21 + A22, B11,        half)   // (c+d)e
    P3 ← HYBRID-STRASSEN(A11,       B12 - B22,  half)   // a(f-h)
    P4 ← HYBRID-STRASSEN(A22,       B21 - B11,  half)   // d(g-e)
    P5 ← HYBRID-STRASSEN(A11 + A12, B22,        half)   // (a+b)h
    P6 ← HYBRID-STRASSEN(A21 - A11, B11 + B12,  half)   // (c-a)(e+f)
    P7 ← HYBRID-STRASSEN(A12 - A22, B21 + B22,  half)   // (b-d)(g+h)

    // Reconstruct result submatrices
    C11 ← P1 + P4 - P5 + P7
    C12 ← P3 + P5
    C21 ← P2 + P4
    C22 ← P1 - P2 + P3 + P6

    return COMBINE(C11, C12, C21, C22)


CONVENTIONAL-MULTIPLY(A, B, n):
─────────────────────────────────
    C ← zero matrix of size n × n

    for i ← 0 to n - 1:
        for j ← 0 to n - 1:
            for k ← 0 to n - 1:
                C[i][j] ← C[i][j] + A[i][k] × B[k][j]

    return C


SPLIT(M, half):
────────────────
    // Split matrix M into four half × half submatrices
    M11 ← M[0 .. half-1][0 .. half-1]        // Top-left
    M12 ← M[0 .. half-1][half .. n-1]        // Top-right
    M21 ← M[half .. n-1][0 .. half-1]        // Bottom-left
    M22 ← M[half .. n-1][half .. n-1]        // Bottom-right
    return M11, M12, M21, M22


COMBINE(C11, C12, C21, C22):
──────────────────────────────
    // Assemble four submatrices into one result matrix
    C ← matrix of size n × n
    C[0..half-1][0..half-1]     ← C11
    C[0..half-1][half..n-1]     ← C12
    C[half..n-1][0..half-1]     ← C21
    C[half..n-1][half..n-1]     ← C22
    return C


### 2×2 Strassen Example (from Case Study)
#
#   A = [[1, 7], [3, 5]]     a=1, b=7, c=3, d=5
#   B = [[1, 3], [7, 5]]     e=1, f=3, g=7, h=5
#
#   P1 = (1+5)(1+5) = 6×6  = 36
#   P2 = (3+5)(1)   = 8×1  =  8
#   P3 = 1×(3-5)   = 1×-2 = -2
#   P4 = 5×(7-1)   = 5×6  = 30
#   P5 = (1+7)(5)  = 8×5  = 40
#   P6 = (3-1)(1+3)= 2×4  =  8
#   P7 = (7-5)(7+5)= 2×12 = 24
#
#   C11 = 36+30-40+24 = 50
#   C12 = -2+40       = 38
#   C21 = 8+30        = 38
#   C22 = 36-8-2+8    = 34
#
#   C = [[50, 38], [38, 34]]  ✅ Verified against conventional multiplication
