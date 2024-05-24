def matrix_chain_order(dims):
    n = len(dims)
    p = [dims[0][0]] + [dims[i][1] for i in range(n)]
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    
    def get_order(s, i, j):
        if i == j:
            return f"M{i+1}"
        return f"({get_order(s, i, s[i][j])} x {get_order(s, s[i][j]+1, j)})"
    
    return get_order(s, 0, n-1), m[0][n-1]

# مثال:
if __name__ == "__main__":
    dims = [[1, 7], [7, 2], [3, 3], [3, 1], [1, 5], [5, 9]]
    order, cost = matrix_chain_order(dims)
    print(f"The optimal order of matrix multiplication is: {order}")
    print(f"The minimum number of multiplications is: {cost}")





