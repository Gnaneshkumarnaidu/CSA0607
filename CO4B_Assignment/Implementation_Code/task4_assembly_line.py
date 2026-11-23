"""
Task 4: Dynamic Programming for Assembly Line Scheduling
Two parallel assembly lines.
"""
def assembly_line_scheduling(a1, a2, t1, t2, e1, e2, x1, x2):
    n = len(a1)
    f1 = [0] * n
    f2 = [0] * n
    l1 = [0] * n
    l2 = [0] * n
    
    f1[0] = e1 + a1[0]
    f2[0] = e2 + a2[0]
    
    trace = []
    
    for j in range(1, n):
        stay_1 = f1[j-1] + a1[j]
        trans_1 = f2[j-1] + t2[j-1] + a1[j]
        if stay_1 <= trans_1:
            f1[j] = stay_1
            l1[j] = 1
        else:
            f1[j] = trans_1
            l1[j] = 2
            
        stay_2 = f2[j-1] + a2[j]
        trans_2 = f1[j-1] + t1[j-1] + a2[j]
        if stay_2 <= trans_2:
            f2[j] = stay_2
            l2[j] = 2
        else:
            f2[j] = trans_2
            l2[j] = 1
            
        trace.append({
            'station': j + 1,
            'stay_1': stay_1, 'trans_1': trans_1, 'sel_1': l1[j],
            'stay_2': stay_2, 'trans_2': trans_2, 'sel_2': l2[j]
        })
        
    exit_1 = f1[n-1] + x1
    exit_2 = f2[n-1] + x2
    if exit_1 <= exit_2:
        opt_time = exit_1
        last_line = 1
    else:
        opt_time = exit_2
        last_line = 2
        
    # Reconstruct route
    route = [last_line]
    curr_line = last_line
    for j in range(n - 1, 0, -1):
        if curr_line == 1:
            curr_line = l1[j]
        else:
            curr_line = l2[j]
        route.append(curr_line)
    route.reverse()
    
    return opt_time, route, trace

if __name__ == '__main__':
    a1 = [4, 5, 3, 2]
    a2 = [2, 10, 1, 4]
    t1 = [7, 4, 2] # 1 to 2
    t2 = [9, 2, 8] # 2 to 1
    e1, e2 = 10, 12
    x1, x2 = 18, 7
    
    tot_time, route, trace = assembly_line_scheduling(a1, a2, t1, t2, e1, e2, x1, x2)
    print(f"Assembly Line Scheduling Baseline:")
    print(f"  Minimum Total Time = {tot_time}")
    print(f"  Optimal Route Sequence = {route}")
    print("  Decision Trace:")
    for t in trace:
        print(f"    Station {t['station']}: Line1(Stay={t['stay_1']}, Trans={t['trans_1']} -> Sel={t['sel_1']}) | Line2(Stay={t['stay_2']}, Trans={t['trans_2']} -> Sel={t['sel_2']})")
