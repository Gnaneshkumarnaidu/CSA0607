"""
Task 6: Last-Mile Delivery Route Optimisation
Held-Karp Dynamic Programming O(n^2 2^n)
"""
import time

def tsp_dp(dist_matrix):
    n = len(dist_matrix)
    # memo[(mask, curr)]: min cost to visit all nodes in mask ending at curr
    memo = {}
    parent = {}
    states_evaluated = [0]

    def solve(mask, u):
        states_evaluated[0] += 1
        if mask == (1 << n) - 1:
            return dist_matrix[u][0] # return to hub 0
            
        state = (mask, u)
        if state in memo:
            return memo[state]
            
        ans = float('inf')
        best_next = -1
        for v in range(n):
            if not (mask & (1 << v)):
                new_cost = dist_matrix[u][v] + solve(mask | (1 << v), v)
                if new_cost < ans:
                    ans = new_cost
                    best_next = v
                    
        parent[state] = best_next
        memo[state] = ans
        return ans

    min_cost = solve(1, 0) # start at hub 0 with mask containing 0
    
    # Reconstruct path
    curr = 0
    mask = 1
    path = [0]
    while mask != (1 << n) - 1:
        next_node = parent[(mask, curr)]
        path.append(next_node)
        mask |= (1 << next_node)
        curr = next_node
    path.append(0) # return to hub
    
    return min_cost, path, states_evaluated[0]

if __name__ == '__main__':
    # Hub (0) + 6 delivery locations (1 to 6) -> 7 total nodes
    dist_matrix = [
        [0, 10, 15, 20, 25, 20, 10],
        [10, 0, 35, 25, 18, 30, 20],
        [15, 35, 0, 30, 28, 40, 15],
        [20, 25, 30, 0, 12, 10, 22],
        [25, 18, 28, 12, 0, 14, 16],
        [20, 30, 40, 10, 14, 0, 25],
        [10, 20, 15, 22, 16, 25, 0]
    ]
    min_cost, path, states = tsp_dp(dist_matrix)
    node_names = ['Hub', 'Loc_A', 'Loc_B', 'Loc_C', 'Loc_D', 'Loc_E', 'Loc_F']
    named_path = [node_names[i] for i in path]
    print("TSP Held-Karp Solution (Hub + 6 Locations):")
    print(f"  Minimum Total Travel Cost: {min_cost}")
    print(f"  Optimal Tour: {' -> '.join(named_path)}")
    print(f"  DP States Evaluated: {states}")
