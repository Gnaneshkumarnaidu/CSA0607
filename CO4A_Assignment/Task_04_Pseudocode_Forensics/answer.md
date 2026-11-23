# TASK 4 – PSEUDOCODE FORENSICS: Find, Explain and Repair an Algorithmic Defect (7 Marks)

### Task 4.1 – Locate the Defect (2 Marks)
The flawed logic is in line 5 of inner loop:
```
IF substring(Text, j, i) is in Dictionary THEN
  DP[i] ← TRUE
  BREAK
END IF
```
**Exact Defect:** The condition only checks if substring $(j, i)$ is in Dictionary, without verifying whether the prefix string before $j$ is validly segmented ($DP[j] == 	ext{TRUE}$). Finding a dictionary word from index $j$ to $i$ is completely useless if the prefix up to $j$ cannot be formed from valid dictionary words!

### Task 4.2 – Construct a Failing Input (2 Marks)
- **Text:** `"catsandog"` ($n=9$).
- **Dictionary:** `{"cats", "dog", "sand", "and", "cat"}`.
- **Trace of Flaw:**
  At $i=9$, the faulty algorithm checks substring $(6, 9) = 	ext{"dog"}$.
  Because `"dog"` is in Dictionary, the algorithm sets $DP[9] \leftarrow 	ext{TRUE}$ and terminates with TRUE.
  However, the prefix from $0$ to $6$ is `"catsan"`, which CANNOT be segmented! The word `"og"` or disjoint characters cannot be formed. The true answer is FALSE.

### Task 4.3 – Repair the Algorithm (2 Marks)
Minimal correction: Add `$DP[j]$ AND` to the condition:
```
ALGORITHM WordBreak_Repaired(Text, Dictionary)
BEGIN
  DP[0] ← TRUE
  FOR i ← 1 TO n DO
    DP[i] ← FALSE
    FOR j ← 0 TO i - 1 DO
      IF DP[j] AND (substring(Text, j, i) is in Dictionary) THEN
        DP[i] ← TRUE
        BREAK
      END IF
    END FOR
  END FOR
  RETURN DP[n]
END
```

### Task 4.4 – Regression Check (1 Mark)
- **Input:** Text: `"leetcode"`, Dictionary: `{"leet", "code"}`.
- **Trace on Repaired:**
  - $i=4$: $j=0 \implies DP[0]=	ext{TRUE}$ and `"leet"` in Dict $\implies DP[4]=	ext{TRUE}$.
  - $i=8$: $j=4 \implies DP[4]=	ext{TRUE}$ and `"code"` in Dict $\implies DP[8]=	ext{TRUE}$.
- **Result:** Returns TRUE, correctly preserving valid behavior.
