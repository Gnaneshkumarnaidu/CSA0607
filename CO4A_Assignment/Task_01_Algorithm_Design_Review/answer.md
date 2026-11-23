# TASK 1 – ALGORITHM DESIGN REVIEW: Diagnose and Repair Poor Pseudocode (6 Marks)

### Problem Context
A delivery vehicle has capacity $W$. Packages have weight $w_i$ and value $v_i$. Packages may be divided fractionally. The objective is to maximize the total value loaded without exceeding capacity $W$.

### Task 1.1 – Diagnose the Design (2 Marks)
The proposed pseudocode:
```
ALGORITHM LoadVehicle
BEGIN
 Read packages
 Arrange packages
 Select the best package
 WHILE vehicle has space DO
  Add suitable package
 END WHILE
 Calculate value
 RETURN result
END
```
**Algorithmic Deficiencies:**
1. **Inputs and Outputs Undefined:** The algorithm signature does not specify parameters (package set $P$, weights $W$, values $V$, knapsack capacity $C$) nor return structures.
2. **Ambiguous Selection Criterion ("best" / "suitable"):** The term "best package" is undefined—it does not state whether it sorts by maximum value $v_i$, minimum weight $w_i$, or value-to-weight density $v_i / w_i$.
3. **No Feasibility Condition or Capacity Tracking:** It does not maintain or decrement remaining capacity $C_{rem}$ as items are placed into the vehicle.
4. **Failure to Handle Fractional Division:** The requirement explicitly states packages may be divided if necessary, but the loop contains no fractional split logic when an item exceeds remaining space.
5. **Indefinite Termination / Potential Infinite Loop:** "WHILE vehicle has space DO" does not specify what happens if all items are packed or if no remaining unpacked package fits, leading to infinite looping or undefined indexing.

### Task 1.2 – Repair the Design (3 Marks)
Rewritten complete, language-independent pseudocode following SIMATS Engineering Standard:
```
ALGORITHM FractionalKnapsack(Packages, Capacity)
INPUT:
  Packages: Array of tuples (id, weight, value) of size n
  Capacity: Real number > 0 representing maximum vehicle capacity
OUTPUT:
  TotalValue: Real number representing maximum value loaded
  Solution: Array of tuples (id, fraction_loaded)

BEGIN
  // Step 1: Compute value-to-weight density for each package
  FOR i ← 1 TO n DO
    density[i] ← Packages[i].value / Packages[i].weight
  END FOR

  // Step 2: Sort packages in descending order of density
  SORT Packages in descending order of density

  // Step 3: Initialize tracking variables
  RemainingCapacity ← Capacity
  TotalValue ← 0.0
  Solution ← EMPTY_LIST()

  // Step 4: Greedy selection loop
  FOR i ← 1 TO n DO
    IF RemainingCapacity = 0 THEN
      BREAK
    END IF

    IF Packages[i].weight <= RemainingCapacity THEN
      // Item completely fits
      RemainingCapacity ← RemainingCapacity - Packages[i].weight
      TotalValue ← TotalValue + Packages[i].value
      APPEND(Solution, (Packages[i].id, 1.0))
    ELSE
      // Item must be fractionally divided to fill exact space
      fraction ← RemainingCapacity / Packages[i].weight
      TotalValue ← TotalValue + (Packages[i].value * fraction)
      APPEND(Solution, (Packages[i].id, fraction))
      RemainingCapacity ← 0
      BREAK
    END IF
  END FOR

  RETURN TotalValue, Solution
END
```

### Task 1.3 – Design Defence (1 Mark)
This rewritten design qualifies as pseudocode rather than programming code because it relies on standard algorithmic notations (such as explicit mathematical loops, clear variable scoping, and high-level abstractions like `SORT ... descending`) without binding to language-specific syntaxes, pointers, or library imports. It avoids informal English by providing exact arithmetic updates, definitive state transitions, and deterministic termination bounds.
