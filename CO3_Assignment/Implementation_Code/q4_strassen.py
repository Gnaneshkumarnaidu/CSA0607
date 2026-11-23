"""
Q4: Strassen's Matrix Multiplication
Algebraic transformation reducing 8 multiplications to 7.
"""
def add_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def sub_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def standard_matmul(A, B, counter):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                counter['mults'] += 1
                C[i][j] += A[i][k] * B[k][j]
    return C

def strassen_matmul(A, B, counter):
    n = len(A)
    if n == 1:
        counter['mults'] += 1
        return [[A[0][0] * B[0][0]]]
    
    mid = n // 2
    a11 = [row[:mid] for row in A[:mid]]
    a12 = [row[mid:] for row in A[:mid]]
    a21 = [row[:mid] for row in A[mid:]]
    a22 = [row[mid:] for row in A[mid:]]

    b11 = [row[:mid] for row in B[:mid]]
    b12 = [row[mid:] for row in B[:mid]]
    b21 = [row[:mid] for row in B[mid:]]
    b22 = [row[mid:] for row in B[mid:]]

    # 7 products
    m1 = strassen_matmul(add_matrix(a11, a22), add_matrix(b11, b22), counter)
    m2 = strassen_matmul(add_matrix(a21, a22), b11, counter)
    m3 = strassen_matmul(a11, sub_matrix(b12, b22), counter)
    m4 = strassen_matmul(a22, sub_matrix(b21, b11), counter)
    m5 = strassen_matmul(add_matrix(a11, a12), b22, counter)
    m6 = strassen_matmul(sub_matrix(a21, a11), add_matrix(b11, b12), counter)
    m7 = strassen_matmul(sub_matrix(a12, a22), add_matrix(b21, b22), counter)

    c11 = add_matrix(sub_matrix(add_matrix(m1, m4), m5), m7)
    c12 = add_matrix(m3, m5)
    c21 = add_matrix(m2, m4)
    c22 = add_matrix(add_matrix(sub_matrix(m1, m2), m3), m6)

    C = []
    for i in range(mid):
        C.append(c11[i] + c12[i])
    for i in range(mid):
        C.append(c21[i] + c22[i])
    return C

if __name__ == '__main__':
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]]
    B = [[8, 7, 6, 5], [4, 3, 2, 1], [1, 2, 3, 4], [5, 6, 7, 8]]
    c_std = {'mults': 0}
    c_str = {'mults': 0}
    res_std = standard_matmul(A, B, c_std)
    res_str = strassen_matmul(A, B, c_str)
    assert res_std == res_str
    print("Matrix Multiplication (4x4):")
    print(f"Standard multiplications: {c_std['mults']} (n^3 = 64)")
    print(f"Strassen multiplications: {c_str['mults']} (7^log2(4) = 49)")
