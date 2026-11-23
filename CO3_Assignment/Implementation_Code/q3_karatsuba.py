"""
Q3: Breaking the Quadratic Barrier: Karatsuba Multiplication
Comparison between grade-school O(n^2) and Karatsuba O(n^1.585)
"""
import time

def standard_multiply(x, y, counter):
    sx = str(x)
    sy = str(y)
    counter['mults'] += len(sx) * len(sy)
    return x * y

def karatsuba(x, y, counter):
    if x < 10 or y < 10:
        counter['mults'] += 1
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)
    
    z0 = karatsuba(low1, low2, counter)
    z1 = karatsuba(low1 + high1, low2 + high2, counter)
    z2 = karatsuba(high1, high2, counter)
    
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

if __name__ == '__main__':
    x = 1234567890123456
    y = 9876543210987654
    c_std = {'mults': 0}
    c_kara = {'mults': 0}
    
    res_std = standard_multiply(x, y, c_std)
    res_kara = karatsuba(x, y, c_kara)
    
    assert res_std == res_kara, "Results mismatch!"
    print(f"Multiplying two 16-digit integers:")
    print(f"Result = {res_std}")
    print(f"Standard Mult Operations: {c_std['mults']}")
    print(f"Karatsuba Recursive Multiplications: {c_kara['mults']}")
