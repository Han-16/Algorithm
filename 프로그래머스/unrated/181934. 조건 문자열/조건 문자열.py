def solution(ineq, eq, n, m):
    # ineq :  > | <
    # eq   :  ! | =
    if ineq == ">":
        if eq == "!":
            return 1 if n > m else 0
        else:
            return 1 if n >= m else 0
    else:
        if eq == "!":
            return 1 if n < m else 0
        else:
            return 1 if n <= m else 0
            
    