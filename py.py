def matrix_chain_order(p):
    n = len(p) - 1  # number of matrices
    m = [[0 for _ in range(n)] for _ in range(n)]  # minimum number of multiplications
    s = [[0 for _ in range(n)] for _ in range(n)]  # index of the optimal split

    for l in range(2, n + 1):  # l is the chain length
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k  # index of the optimal split

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i + 1}", end='')
    else:
        print("(", end='')
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end='')

# dimensions of the matrices
p = [1, 7, 2, 3, 1, 5, 9]

m, s = matrix_chain_order(p)
print("Minimum number of multiplications is", m[0][len(p) - 2])

print("The optimal parenthesization is:", end=' ')
print_optimal_parens(s, 0, len(p) - 2)
