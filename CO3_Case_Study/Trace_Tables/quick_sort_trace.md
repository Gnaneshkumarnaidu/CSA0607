# Quick Sort Trace Table
# Module 2: Live Seller Leaderboard
# KartIQ – Retail Data Analytics Platform | CO3 Case Study

## Input Data
Seller scores: [42, 17, 63, 8, 55, 29]
Pivot: 42 (first element, Hoare-style partitioning)

---

## Partition Trace – First Level

**Initial state:**

| Index | 0 | 1 | 2 | 3 | 4 | 5 |
|-------|---|---|---|---|---|---|
| Value | **42** | 17 | 63 | 8 | 55 | 29 |
| Role | PIVOT | — | — | — | — | — |

Convention: L pointer starts at index 1 (after pivot), R pointer at index 5.

| Step | L idx | R idx | A[L] | A[R] | Action | Array State |
|------|-------|-------|------|------|--------|-------------|
| Start | 1 | 5 | 17 | 29 | L=1: 17≤42, advance L | [42, 17, 63, 8, 55, 29] |
| 1 | 2 | 5 | 63 | 29 | L=2: 63>42, STOP L; R=5: 29≤42, STOP R | [42, 17, 63, 8, 55, 29] |
| Swap | 2 | 5 | — | — | Swap A[2] and A[5] | [42, 17, **29**, 8, 55, **63**] |
| 2 | 3 | 4 | 8 | 55 | L=3: 8≤42, advance L | [42, 17, 29, 8, 55, 63] |
| 3 | 4 | 4 | 55 | 55 | L=4: 55>42, STOP L; R=4: 55>42, move R left | [42, 17, 29, 8, 55, 63] |
| 4 | 4 | 3 | — | 8 | L=4 > R=3: partition done | [42, 17, 29, 8, 55, 63] |
| Pivot swap | 0 | 3 | — | — | Swap pivot A[0]=42 with A[R=3]=8 | [**8**, 17, 29, **42**, 55, 63] |

**After first partition:**

| Index | 0 | 1 | 2 | 3 | 4 | 5 |
|-------|---|---|---|---|---|---|
| Value | 8 | 17 | 29 | **42** | 55 | 63 |
| Partition | Left (<42) | Left | Left | PIVOT (final) | Right (>42) | Right |

**Pivot 42 is now at index 3 — its final sorted position. ✅**

---

## Recursive Application (Full Sort)

```
Level 0:  [42, 17, 63, 8, 55, 29]
          After partition pivot=42: [8, 17, 29] | 42 | [55, 63]

Level 1 (Left):  [8, 17, 29]
          Pivot=8: [] | 8 | [17, 29]
Level 1 (Right): [55, 63]
          Pivot=55: [] | 55 | [63]

Level 2: [17, 29]
          Pivot=17: [] | 17 | [29]

Level 3: [29] ← base case

Final sorted: [8, 17, 29, 42, 55, 63]
```

---

## Worst Case Illustration – Nearly Sorted Input

Input: [8, 17, 29, 42, 55, 63] (already sorted, first-element pivot)

| Call | Pivot | Left partition | Right partition | Partition size |
|------|-------|---------------|-----------------|----------------|
| 1 | 8 | [] (0 elements) | [17,29,42,55,63] (5 elements) | 0 vs 5 |
| 2 | 17 | [] (0 elements) | [29,42,55,63] (4 elements) | 0 vs 4 |
| 3 | 29 | [] (0 elements) | [42,55,63] (3 elements) | 0 vs 3 |
| 4 | 42 | [] (0 elements) | [55,63] (2 elements) | 0 vs 2 |
| 5 | 55 | [] (0 elements) | [63] (1 element) | 0 vs 1 |

> ❌ **Every partition is maximally unbalanced (0 vs n-1)**  
> This yields T(n) = T(n-1) + Θ(n) → **O(n²) worst case**  
> For 100,000 sellers: ≈ 5 × 10⁹ comparisons → system freeze!

---

## Improved Pivot – Median of Three Example

Input: [8, 17, 29, 42, 55, 63]

Median-of-three candidates: A[0]=8, A[3]=42, A[5]=63
Sorted: 8 ≤ 42 ≤ 63 → **Median = 42**

| Call | Pivot | Left partition | Right partition | Balance |
|------|-------|---------------|-----------------|---------|
| 1 | 42 | [8,17,29] (3 elem) | [55,63] (2 elem) | Good (3 vs 2) |

> ✅ **Balanced partition → O(n log n) expected performance**
