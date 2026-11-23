# CO3 Case Study – KartIQ Retail Data Analytics Platform
# Design and Analysis of Algorithms (CSA0607)

## Overview

This folder contains the complete CO3 Case Study assignment for the subject Design and Analysis of Algorithms (Course Code: CSA0607). The case study analyses the **KartIQ – Retail Data Analytics Platform** and demonstrates how Divide-and-Conquer algorithms solve real-world performance challenges at scale.

---

## Folder Structure

```
CO3_Case_Study/
├── Report/
│   └── CO3_Case_Study_Report.md       ← Complete assignment (main document)
├── Pseudocode/
│   ├── merge_sort_stable.md           ← Stable Merge Sort pseudocode (Module 1)
│   ├── quick_sort_improved.md         ← Improved Quick Sort pseudocode (Module 2)
│   ├── binary_search_lower_bound.md   ← Binary Search pseudocode (Module 3)
│   └── strassen_hybrid.md             ← Hybrid Strassen pseudocode (Module 4)
├── Trace_Tables/
│   ├── merge_sort_trace.md            ← Step-by-step Merge Sort trace
│   └── quick_sort_trace.md            ← Step-by-step Quick Sort trace
└── README.md                          ← This file
```

---

## Modules Covered

| Module | Algorithm | Complexity |
|--------|-----------|------------|
| 1 – Nightly Order Consolidation | Stable Merge Sort | Θ(n log n) |
| 2 – Live Seller Leaderboard | Quick Sort (Median-of-Three + 3-Way) | Θ(n log n) avg |
| 3 – Order Lookup | Lower-Bound Binary Search | Θ(log n) |
| 4 – Recommendation Scores | Hybrid Strassen Matrix Multiplication | O(n^2.807) |

---

## Key Mathematical Results

| Analysis | Result |
|----------|--------|
| Merge Sort comparisons (10M orders) | ≈ 232,500,000 |
| Binary Search comparisons (10M orders) | ≤ 24 |
| Quick Sort worst case (100K sellers, sorted input) | ≈ 5 × 10⁹ |
| Conventional multiplication (1024×1024) | 1,073,741,824 ops |
| Strassen multiplication (1024×1024) | 282,475,249 ops (~74% reduction) |

---

## Assignment Questions Covered

- **(a)** Understanding the Case – Module comparison table + Divide-and-Conquer role
- **(b)** Module 1 – Merge Sort with stability proof and full trace
- **(c)** Module 2 – Quick Sort with pivot analysis and worst-case explanation
- **(d)** Module 3 – Binary Search with first-occurrence (lower-bound) variant
- **(e)** Module 4 – Strassen's Matrix Multiplication with full 2×2 worked example
- **(f)** Final System Design – Integrated architecture and justification table

---

## Assessment Details

- **Course Code:** CSA0607
- **Assessment:** CO3 – Case Study
- **Topic:** Divide-and-Conquer Engine of a Retail Data Analytics Platform
- **Mode:** Individual | **Duration:** 1 Week
- **Target Level:** Level 4 – Exemplary
