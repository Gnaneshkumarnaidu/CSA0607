"""
Task 2: Greedy vs Dynamic Programming Knapsack
Fractional Knapsack (Greedy) vs 0/1 Knapsack (DP)
"""
def fractional_knapsack(items, capacity):
    # items: list of (id, weight, value)
    sorted_items = sorted(items, key=lambda x: x[2]/x[1], reverse=True)
    rem = capacity
    tot_val = 0.0
    selected = []
    comparisons = 0
    
    for item in sorted_items:
        iid, w, v = item
        if rem == 0:
            break
        if w <= rem:
            rem -= w
            tot_val += v
            selected.append((iid, 1.0, v))
        else:
            frac = rem / w
            tot_val += v * frac
            selected.append((iid, frac, v * frac))
            rem = 0
            break
    return tot_val, selected

def knapsack_01_dp(items, capacity):
    n = len(items)
    dp = [[0]*(capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        iid, w, v = items[i - 1]
        for c in range(1, capacity + 1):
            if w > c:
                dp[i][c] = dp[i-1][c]
            else:
                dp[i][c] = max(dp[i-1][c], dp[i-1][c - w] + v)
                
    curr_c = capacity
    selected = []
    for i in range(n, 0, -1):
        if dp[i][curr_c] != dp[i-1][curr_c]:
            iid, w, v = items[i - 1]
            selected.append((iid, 1.0, v))
            curr_c -= w
    selected.reverse()
    return dp[n][capacity], selected

if __name__ == '__main__':
    # Normal Case where greedy intuition is near-optimal
    items_norm = [('A', 10, 60), ('B', 20, 100), ('C', 30, 120)]
    cap_norm = 50
    f_val, f_sel = fractional_knapsack(items_norm, cap_norm)
    dp_val, dp_sel = knapsack_01_dp(items_norm, cap_norm)
    print(f"Normal Case (Capacity={cap_norm}):")
    print(f"  Fractional Greedy: Val={f_val}, Items={f_sel}")
    print(f"  0/1 DP: Val={dp_val}, Items={dp_sel}")
    
    # Counterexample: Break the Greedy Intuition in 0/1 Knapsack
    # Greedy by value/weight picks Item 1 (density 6), filling 10, leaving 20 capacity, cannot take Item 2 and 3
    items_counter = [('Item1', 10, 60), ('Item2', 20, 100), ('Item3', 20, 100)] # Densities: 6.0, 5.0, 5.0
    cap_counter = 40
    # Greedy for 0/1: takes Item1 (10kg, val 60) + Item2 (20kg, val 100) -> 30kg, val 160. Leaves 10kg empty.
    # DP optimal: takes Item2 (20kg) + Item3 (20kg) -> 40kg, val 200!
    dp_c_val, dp_c_sel = knapsack_01_dp(items_counter, cap_counter)
    print(f"\nCounterexample Case (Capacity={cap_counter}):")
    print(f"  Greedy 0/1 commitment to Item1 yields value 160.")
    print(f"  0/1 DP Optimum Value: {dp_c_val}, Items={dp_c_sel}")
