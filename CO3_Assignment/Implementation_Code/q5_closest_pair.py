"""
Q5: Closest Pair of Points using Divide and Conquer O(n log n)
Compared against Brute-Force O(n^2)
"""
import math

def dist(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def brute_force_closest(points, counter):
    min_d = float('inf')
    best_pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            counter['dist_calc'] += 1
            d = dist(points[i], points[j])
            if d < min_d:
                min_d = d
                best_pair = (points[i], points[j])
    return min_d, best_pair

def closest_pair_rec(px, py, counter):
    n = len(px)
    if n <= 3:
        return brute_force_closest(px, counter)
    
    mid = n // 2
    mid_point = px[mid]
    
    qx = px[:mid]
    rx = px[mid:]
    
    mid_x = mid_point[0]
    qy = [p for p in py if p[0] <= mid_x]
    ry = [p for p in py if p[0] > mid_x]
    
    d1, pair1 = closest_pair_rec(qx, qy, counter)
    d2, pair2 = closest_pair_rec(rx, ry, counter)
    
    if d1 < d2:
        d = d1
        best_pair = pair1
    else:
        d = d2
        best_pair = pair2
        
    strip = [p for p in py if abs(p[0] - mid_point[0]) < d]
    
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 8, len(strip))):
            counter['dist_calc'] += 1
            d_strip = dist(strip[i], strip[j])
            if d_strip < d:
                d = d_strip
                best_pair = (strip[i], strip[j])
                
    return d, best_pair

def closest_pair_dc(points, counter):
    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    return closest_pair_rec(px, py, counter)

if __name__ == '__main__':
    pts = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4), (20, 15), (25, 40), (8, 9), (15, 22)]
    c_bf = {'dist_calc': 0}
    c_dc = {'dist_calc': 0}
    d_bf, p_bf = brute_force_closest(pts, c_bf)
    d_dc, p_dc = closest_pair_dc(pts, c_dc)
    print(f"Closest Pair Brute Force: dist = {d_bf:.4f}, pairs = {p_bf}, Dist Calcs = {c_bf['dist_calc']}")
    print(f"Closest Pair D&C: dist = {d_dc:.4f}, pairs = {p_dc}, Dist Calcs = {c_dc['dist_calc']}")
