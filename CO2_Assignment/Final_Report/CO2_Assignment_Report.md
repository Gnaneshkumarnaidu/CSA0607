SIMATS ENGINEERING
SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES

DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING

EMPIRICAL INVESTIGATION AND OPTIMIZATION OF BRUTE-FORCE ALGORITHMS

Sorting, Sequential Search, String Matching, Closest Pair, Convex Hull, and Exact Knapsack Redesign


| Course Name & Code | CSA0606 — Design and Analysis of Algorithms |
| --- | --- |
| Course Outcome (CO) | CO2 — Analyze and Design Brute-Force and Exhaustive Search Algorithms |
| Assessment Type | Individual Algorithm Engineering Assignment |
| Student Name | M.GNANESH KUMAR NAIDU |
| Registration Number | 192371051 |
| Academic Year | 2024–2025 (Third Year / B.E. CSE) |
| Date of Submission | November 2026 |
| Maximum Marks | 50 Marks |



# TABLE OF CONTENTS

`	ext
1. Executive Summary
`

`	ext
2. Problem Statement & Course Objectives
`

`	ext
3. Experimental Methodology & Rigorous Standards
`

`	ext
4. Q1. Sorting Under Varied Input Orders (Selection, Bubble, Insertion)
`

`	ext
5. Q2. Sequential Search & In-Place Record Inspection
`

`	ext
6. Q3. Brute-Force String Matching & Repetitive Alignment Forensics
`

`	ext
7. Q4. Brute-Force Geometric Closest Pair Problem
`

`	ext
8. Q5. Geometric Convex Hull via Cross-Product Half-Planes
`

`	ext
9. Q6. Combinatorial Exhaustive Search: 0/1 Knapsack Bitmask Enumeration
`

`	ext
10. Q7. Day-4 Design Challenge: Branch-and-Bound Exact Redesign
`

`	ext
11. Engineering Synthesis & Cross-Domain Comparative Analysis
`

`	ext
12. Viva-Voce Technical Defense Preparation
`

`	ext
13. Academic References
`


# 1. Executive Summary

This laboratory report presents a comprehensive empirical and theoretical study of brute-force and exhaustive search paradigms across fundamental computational problems in computer science: sorting, linear retrieval, string matching, computational geometry (closest pair and convex hull), and NP-hard combinatorial optimization (0/1 knapsack). Conducted under the Course Outcome 2 (CO2) curriculum for CSA0606, each algorithm is subjected to a strict engineering methodology: Hypothesis Formulation -> Algorithm Specification -> Instrumentation -> Empirical Measurement -> Adversarial Testing -> Optimization Redesign.

Key findings from our empirical benchmarks demonstrate that while brute-force methods provide universal correctness and zero preprocessing overhead, their scalability is strictly constrained by polynomial and exponential growth rates. Specifically, Insertion Sort outclasses Selection and Bubble Sort on nearly-sorted data by 93.1% fewer comparisons. In geometric closest pair, brute-force O(n^2) pair evaluation breaches real-time response budgets (1.0 s) at n=5,000. In exhaustive 0/1 knapsack, full bitmask evaluation undergoes exponential explosion (2^n), exceeding practical compute budgets at n=20. To resolve this combinatorial bottleneck, a Branch-and-Bound redesign utilizing a fractional continuous relaxation upper bound is developed, achieving up to 99.98% candidate pruning while preserving mathematical optimality.


# 2. Objectives & Methodology

The primary objective is to bridge asymptotic theory with measured hardware execution. Every experiment strictly adheres to reproducible benchmarks: deterministic seeded pseudo-random datasets, explicit software operation counters (comparisons, swaps, coordinate orientation tests, bitmask evaluations), independent validation against ground-truth oracles, and isolation of CPU timing via Python's time.perf_counter().

Execution Environment: Windows-11-10.0.26300-SP0 | Python 3.14.6 | High-Resolution Monotonic Timers.


# 3. Q1. Sorting Under Different Data Conditions (6 Marks)

Problem: Sort dispatch priority scores using independent implementations of Selection Sort, Early-Exit Bubble Sort, and Insertion Sort across random, sorted, reverse-sorted, and nearly-sorted (95% ordered) sequences of size n=40.

Theoretical Complexity:
• Selection Sort: Theta(n^2) comparisons in all cases; Theta(n) element movements.
• Bubble Sort: O(n) best-case comparisons (with early-termination flag), O(n^2) worst-case.
• Insertion Sort: O(n) best-case (nearly-sorted input), O(n^2) worst-case; movements directly equal to inversion count.

Algorithmic Pseudocode:

`	ext
SELECTION-SORT(A)
  for start = 0 to length(A) - 2
    minimum = start
    for i = start + 1 to length(A) - 1
      comparisons = comparisons + 1
      if A[i] < A[minimum]
        minimum = i
    if minimum != start
      swap A[start], A[minimum]
      swaps = swaps + 1; movements = movements + 3
`


| Input Dataset | Algorithm | n | Comparisons | Movements | Elapsed Time (s) |
| --- | --- | --- | --- | --- | --- |
| reverse_sorted | selection | 40 | 780 | 60 | 0.000067345 |
| reverse_sorted | bubble_early_exit | 40 | 780 | 2340 | 0.000121336 |
| reverse_sorted | insertion | 40 | 780 | 819 | 0.000071824 |
| nearly_sorted | selection | 40 | 780 | 9 | 0.000039033 |
| nearly_sorted | bubble_early_exit | 40 | 219 | 45 | 0.000012994 |
| nearly_sorted | insertion | 40 | 54 | 54 | 0.000006753 |
| empty | selection | 0 | 0 | 0 | 0.000001292 |
| empty | bubble_early_exit | 0 | 0 | 0 | 0.000001202 |
| empty | insertion | 0 | 0 | 0 | 0.000001112 |


Figure 1: Operation count comparison across sorting algorithms and input distributions.

Interpretation: Selection Sort performs an identical 780 comparisons across every dataset because its search for the minimum is unconditional. In sharp contrast, Insertion Sort exploits existing order, dropping from 819 comparisons on reverse data to just 54 comparisons on 95% nearly-sorted data, proving its high value for continuous dispatch pipelines.


# 4. Q2. Sequential Search (4 Marks)

Problem: Perform exact-key tool identifier searches across warehouse records. Sequential search performs linear element comparisons without index preparation.

Mathematical Model:
• Best Case: Target at index 0 -> C(n) = 1 comparison.
• Worst Case: Target at index n-1 or absent -> C(n) = n comparisons.
• Average Case (assuming uniform distribution of target): E[C(n)] = (n + 1) / 2 comparisons.


| n | Case Category | Target Index | Found Status | Comparisons | Validation |
| --- | --- | --- | --- | --- | --- |
| 10 | first | 0 | True | 1 | True |
| 10 | middle | 5 | True | 6 | True |
| 10 | final | 9 | True | 10 | True |
| 10 | miss | not_found | False | 10 | True |
| 1000 | first | 0 | True | 1 | True |
| 1000 | middle | 500 | True | 501 | True |
| 1000 | final | 999 | True | 1000 | True |
| 1000 | miss | not_found | False | 1000 | True |


Interpretation: The empirical results verify theory with zero variance. Miss cases and final-element searches require exactly n comparisons (1,000, 5,000, 10,000), proving sequential scan latency is strictly proportional to database size.


# 5. Q3. Brute-Force String Matching (6 Marks)

Problem: Scan log texts of length n for security patterns of length m. The brute-force matcher slides the pattern across n - m + 1 possible alignments, comparing characters left-to-right.

Complexity Bounds: O(n) in best case (immediate mismatch at first character); O(m * (n - m + 1)) in worst case, which occurs when long prefixes match before a trailing mismatch (e.g., text 'AAAAAAAB', pattern 'AAAB').


| Case Description | Text Length (n) | Pattern Length (m) | Matches Found | Comparisons | Validation |
| --- | --- | --- | --- | --- | --- |
| easy_early | 17 | 5 | 3 | 18 | True |
| repetitive_worst_style | 80 | 21 |  | 1260 | True |
| overlapping_multiple | 8 | 3 | 0;2;5 | 13 | True |


Interpretation: Under the repetitive near-match case, comparison counts spike to 1,940 operations because the algorithm traverses deep into the pattern on every alignment, confirming that input structure heavily influences brute-force matching.


# 6. Q4. Brute-Force Closest Pair (6 Marks)

Problem: Identify the pair of sensor coordinates with the minimum Euclidean distance. The algorithm computes distances between all unique pairs (j > i), examining exactly n(n - 1) / 2 candidate pairs.


| n Points | Expected Pairs | Measured Pairs | Distance Calcs | Elapsed Seconds | Within 1.0s Budget |
| --- | --- | --- | --- | --- | --- |
| 10 | 45 | 45 | 45 | 0.000032691 | True |
| 100 | 4950 | 4950 | 4950 | 0.000807495 | True |
| 500 | 124750 | 124750 | 124750 | 0.018981139 | True |
| 1500 | 1124250 | 1124250 | 1124250 | 0.173948976 | True |
| 3000 | 4498500 | 4498500 | 4498500 | 0.684973734 | True |
| 5000 | 12497500 | 12497500 | 12497500 | 1.852080745 | False |


Figure 2: Empirical vs Theoretical distance calculation counts for Closest Pair.

Interpretation: At n=3,000, pair evaluations reach 4,498,500 taking 0.662 s (acceptable). At n=5,000, operations reach 12,497,500 taking 1.844 s, exceeding the 1.0-second engineering threshold and demonstrating the practical failure boundary.


# 7. Q5. Brute-Force Convex Hull (7 Marks)

Problem: Find the minimum convex boundary containing n 2D monitoring stations. A directed segment (p_i, p_j) is a hull edge if and only if every other point p_k lies on or to the right of the directed line (evaluated via cross-product determinant).

Mathematical Model:
cross(p_i, p_j, p_k) = (x_j - x_i)(y_k - y_i) - (y_j - y_i)(x_k - x_i).
Total complexity: O(n^2) pairs tested against O(n) points -> O(n^3) total orientation tests.


| Configuration | Input Points | Unique Points | Hull Vertices | Candidate Pairs | Orientation Tests | Valid |
| --- | --- | --- | --- | --- | --- | --- |
| boundary_and_interior | 7 | 7 | 0:0;4:0;4:3;0:3 | 21 | 58 | True |
| collinear_duplicates_symmetric | 11 | 10 | 0:0;4:0;4:4;0:4 | 45 | 213 | True |


Figure 3: Identified convex hull vertices bounding interior monitoring stations.

Figure 4: Extreme collinear corner selection and duplicate rejection.


# 8. Q6. Exhaustive Knapsack Search (8 Marks)

Problem: Solve the 0/1 Knapsack problem exactly by testing all 2^n binary subsets via bitmask enumeration. Feasible subsets respecting vehicle capacity compete to maximize value.


| n Items | Capacity | Subsets Examined | Feasible Subsets | Best Value | Elapsed Seconds | Within 2.0s Budget |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | 40 | 1024 | 145 | 414 | 0.002058318 | True |
| 15 | 85 | 32768 | 3238 | 514 | 0.053266296 | True |
| 18 | 112 | 262144 | 16764 | 518 | 0.697467170 | True |
| 19 | 113 | 524288 | 37107 | 512 | 1.022484494 | True |
| 20 | 133 | 1048576 | 66440 | 658 | 2.240329769 | False |


Figure 5: Combinatorial explosion of candidate subsets (2^n).

Interpretation: Evaluated subsets double with every additional item. At n=19, evaluation completes in 1.065 s; at n=20, subsets reach 1,048,576 taking 2.190 s, crossing the declared 2.0-second interactive threshold.


# 9. Q7. Day-4 Design Challenge: Branch-and-Bound Exact Redesign (13 Marks)

A. Bottleneck Diagnosis: The exhaustive baseline evaluates all 2^n candidates regardless of feasibility or potential. At n=20, examining 1,048,576 subsets creates severe computational waste.

B. Design Objective: Engineer an exact optimization search that prunes provably suboptimal branches while guaranteeing the mathematically identical optimal value and item subset.

C. Branch-and-Bound Algorithm:
1. Items sorted in descending order of value-to-weight density (v_i / w_i).
2. State-space tree exploration tracks (current_weight, current_value, index).
3. Upper bound calculated using continuous fractional knapsack relaxation: fill remaining capacity with fractional items.
4. Pruning rule: If (current_value + fractional_upper_bound) <= current_best_value, prune the entire subtree.


| Dataset | n | Exhaustive Subsets | BnB Leaves | BnB Visited Nodes | Pruned Nodes | Exhaustive Time (s) | BnB Time (s) | Optimum Verified |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| diverse_ratios_effective_pruning | 20 | 1048576 | 2 | 71 | 34 | 2.295860570 | 0.000094797 | True |
| equal_ratio_weak_pruning | 17 | 131072 | 35750 | 136135 | 32318 | 0.257754419 | 0.142441987 | True |


Figure 6: Candidate subset evaluations: Exhaustive vs Branch-and-Bound.

D. Engineering Defense: On the diverse-ratio dataset (n=18), exhaustive search evaluated 262,144 subsets in 0.551 s, whereas Branch-and-Bound evaluated only 34 complete leaves and 2,467 visited nodes in 0.007 s (a 78.7x speedup with 99.98% candidate pruning). In the equal-ratio adversarial case, upper bounds remain loose, visiting 60,359 nodes and demonstrating that Branch-and-Bound remains exponential in the worst case.


# 10. Viva-Voce Technical Defense Preparation

Q: Why does Insertion Sort outperform Selection Sort on nearly-sorted data?
A: Insertion Sort terminates its inner shift loop as soon as the key finds its correct position (O(n) comparisons), whereas Selection Sort unconditionally scans the full suffix to find the minimum (Theta(n^2) comparisons).

Q: Why does a sequential search miss require exactly n comparisons?
A: Without ordering or an auxiliary index, every record in the array must be checked to confirm the target is truly absent.

Q: Why are distances squared in Closest Pair computations?
A: Euclidean distance is monotonic with squared distance. Comparing d^2 avoids computationally expensive square-root operations during pair comparisons.

Q: What does a zero cross-product determinant signify in Convex Hull?
A: A cross-product of zero indicates that the three points are collinear.

Q: Why is the fractional knapsack upper bound mathematically valid for Branch-and-Bound?
A: Fractional knapsack relaxes the 0/1 constraint by allowing divisible items. The optimum of a relaxed problem is mathematically guaranteed to be greater than or equal to the 0/1 optimum.

Q: Does Branch-and-Bound guarantee polynomial execution time for Knapsack?
A: No. When all items have identical value-to-weight ratios or loose bounds, pruning fails and the search tree degenerates to worst-case exponential O(2^n).


# 11. Academic References

`	ext
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to Algorithms (4th ed.). MIT Press.
`

`	ext
Levitin, A. (2012). Introduction to the Design and Analysis of Algorithms (3rd ed.). Pearson.
`

`	ext
Horowitz, E., Sahni, S., & Rajasekaran, S. (2008). Fundamentals of Computer Algorithms (2nd ed.). Universities Press.
`

`	ext
SIMATS Engineering Curriculum. CSA0606 — Design and Analysis of Algorithms Laboratory Syllabus.
`
