# Merge Sort Trace Tables
# Module 1: Nightly Order Consolidation
# KartIQ – Retail Data Analytics Platform | CO3 Case Study

## Input Data

| Index | Timestamp | Order ID |
|-------|-----------|----------|
| 0 | 105 | O1 |
| 1 | 102 | O2 |
| 2 | 105 | O3 |
| 3 | 101 | O4 |
| 4 | 102 | O5 |
| 5 | 103 | O6 |

---

## Division Phase

```
Level 0:  [(105,O1) (102,O2) (105,O3) | (101,O4) (102,O5) (103,O6)]
           Indices 0,1,2                 Indices 3,4,5

Level 1 (Left):   [(105,O1) (102,O2) | (105,O3)]
                   Indices 0,1          Index 2

Level 1 (Right):  [(101,O4) (102,O5) | (103,O6)]
                   Indices 3,4          Index 5

Level 2 (LL):     [(105,O1) | (102,O2)]
                   Index 0     Index 1

Level 2 (LR):     [(105,O3)]  ← base case
                   Index 2

Level 2 (RL):     [(101,O4) | (102,O5)]
                   Index 3     Index 4

Level 2 (RR):     [(103,O6)]  ← base case
                   Index 5

Level 3 (LLL):    [(105,O1)]  ← base case
Level 3 (LLR):    [(102,O2)]  ← base case
Level 3 (RLL):    [(101,O4)]  ← base case
Level 3 (RLR):    [(102,O5)]  ← base case
```

---

## Merge Phase – Detailed Trace Tables

### Merge 1: [(105,O1)] + [(102,O2)]

| Step | L pointer | R pointer | Comparison | Decision | Output |
|------|-----------|-----------|------------|----------|--------|
| 1 | (105,O1) | (102,O2) | 105 > 102 | Place R: (102,O2) | (102,O2) |
| 2 | (105,O1) | — | R exhausted | Place remaining L | (105,O1) |

**Result: [(102,O2) (105,O1)]**

---

### Merge 2: [(102,O2) (105,O1)] + [(105,O3)]

| Step | L pointer | R pointer | Comparison | Decision | Output |
|------|-----------|-----------|------------|----------|--------|
| 1 | (102,O2) | (105,O3) | 102 < 105 | Place L: (102,O2) | (102,O2) |
| 2 | (105,O1) | (105,O3) | **105 = 105** | **Equal → Place L: (105,O1) ← STABILITY** | (105,O1) |
| 3 | — | (105,O3) | L exhausted | Place remaining R | (105,O3) |

**Result: [(102,O2) (105,O1) (105,O3)]**

> ✅ **Stability demonstrated:** (105,O1) placed before (105,O3) because O1 came first in the original input (left subarray).

---

### Merge 3: [(101,O4)] + [(102,O5)]

| Step | L pointer | R pointer | Comparison | Decision | Output |
|------|-----------|-----------|------------|----------|--------|
| 1 | (101,O4) | (102,O5) | 101 < 102 | Place L: (101,O4) | (101,O4) |
| 2 | — | (102,O5) | L exhausted | Place remaining R | (102,O5) |

**Result: [(101,O4) (102,O5)]**

---

### Merge 4: [(101,O4) (102,O5)] + [(103,O6)]

| Step | L pointer | R pointer | Comparison | Decision | Output |
|------|-----------|-----------|------------|----------|--------|
| 1 | (101,O4) | (103,O6) | 101 < 103 | Place L: (101,O4) | (101,O4) |
| 2 | (102,O5) | (103,O6) | 102 < 103 | Place L: (102,O5) | (102,O5) |
| 3 | — | (103,O6) | L exhausted | Place remaining R | (103,O6) |

**Result: [(101,O4) (102,O5) (103,O6)]**

---

### Final Merge: [(102,O2) (105,O1) (105,O3)] + [(101,O4) (102,O5) (103,O6)]

| Step | L pointer | R pointer | Comparison | Decision | Output |
|------|-----------|-----------|------------|----------|--------|
| 1 | (102,O2) | (101,O4) | 102 > 101 | Place R: (101,O4) | (101,O4) |
| 2 | (102,O2) | (102,O5) | **102 = 102** | **Equal → Place L: (102,O2) ← STABILITY** | (102,O2) |
| 3 | (105,O1) | (102,O5) | 105 > 102 | Place R: (102,O5) | (102,O5) |
| 4 | (105,O1) | (103,O6) | 105 > 103 | Place R: (103,O6) | (103,O6) |
| 5 | (105,O1) | — | R exhausted | Place remaining L | (105,O1) |
| 6 | (105,O3) | — | R exhausted | Place remaining L | (105,O3) |

**Final Sorted Output:**

| Index | Timestamp | Order ID | Notes |
|-------|-----------|----------|-------|
| 0 | 101 | O4 | — |
| 1 | 102 | O2 | ← First 102 (arrived before O5) ✅ |
| 2 | 102 | O5 | ← Second 102 ✅ |
| 3 | 103 | O6 | — |
| 4 | 105 | O1 | ← First 105 (arrived before O3) ✅ |
| 5 | 105 | O3 | ← Second 105 ✅ |

> ✅ **Stability fully verified:** All equal-timestamp pairs maintain their original arrival order.
