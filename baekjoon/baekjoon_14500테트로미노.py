def check_I(i, j):
    I = 0
    I_rotated_90_degrees = 0

    if i + 3 < N:
        I = LST[i][j] + LST[i+1][j] + LST[i+2][j] + LST[i+3][j]  # |

    if j + 3 < M:
        I_rotated_90_degrees = LST[i][j] + LST[i][j+1] + LST[i][j+2] + LST[i][j+3]  # —

    return(max(I, I_rotated_90_degrees))


def check_O(i, j):
    O = 0

    if i + 1 < N and j + 1 < M:
        O = LST[i][j] + LST[i+1][j] + LST[i][j+1] + LST[i+1][j+1]  # □

    return O


def check_T(i, j):
    T = 0
    T_rotated_90_degrees = 0
    T_rotated_180_degrees = 0
    T_rotated_270_degrees = 0

    if i + 1 < N and j + 2 < M:
        T = LST[i][j] + LST[i][j+1] + LST[i][j+2] + LST[i+1][j+1]  # ┬

    if 0 <= i - 1 and i + 1 < N and j + 1 < M:
        T_rotated_90_degrees = LST[i][j] + LST[i-1][j+1] + LST[i][j+1] + LST[i+1][j+1]  # ┤
        T_rotated_270_degrees = LST[i][j] + LST[i-1][j] + LST[i+1][j] + LST[i][j+1]  # ├

    if 0 <= i - 1 and j + 2 < M:
        T_rotated_180_degrees = LST[i][j] + LST[i][j+1] + LST[i][j+2] + LST[i-1][j+1]  # ┴

    return(max(T, T_rotated_90_degrees, T_rotated_180_degrees, T_rotated_270_degrees))


def check_L(i, j):
    L = 0
    L_rotated_90_degrees = 0
    L_rotated_180_degrees = 0
    L_rotated_270_degrees = 0

    if i + 2 < N and j + 1 < M:
        L = LST[i][j] + LST[i+1][j] + LST[i+2][j] + LST[i+2][j+1]  # └
        L_rotated_180_degrees = LST[i][j] + LST[i][j + 1] + LST[i + 1][j + 1] + LST[i + 2][j + 1]  # ┐

    if i + 1 < N and j + 2 < M:
        L_rotated_90_degrees = LST[i][j] + LST[i+1][j] + LST[i][j+1] + LST[i][j+2]  # ┌

    if 0 <= i - 1 and j + 2 < M:
        L_rotated_270_degrees = LST[i][j] + LST[i][j+1] + LST[i][j+2] + LST[i-1][j+2]  # ┘

    return(max(L, L_rotated_90_degrees, L_rotated_180_degrees, L_rotated_270_degrees))


def check_J(i, j):
    J = 0
    J_rotated_90_degrees = 0
    J_rotated_180_degrees = 0
    J_rotated_270_degrees = 0

    if 0 <= i - 2 and j + 1 < M:
        J = LST[i][j] + LST[i][j+1] + LST[i-1][j+1] + LST[i-2][j+1]  # ┘

    if i + 1 < N and j + 2 < M:
        J_rotated_90_degrees = LST[i][j] + LST[i+1][j] + LST[i+1][j+1] + LST[i+1][j+2]  # └
        J_rotated_270_degrees = LST[i][j] + LST[i][j+1] + LST[i][j+2] + LST[i+1][j+2]  # ┐

    if i + 2 < N and j + 1 < M:
        J_rotated_180_degrees = LST[i][j] + LST[i][j+1] + LST[i+1][j] + LST[i+2][j]  # ┌

    return(max(J, J_rotated_90_degrees, J_rotated_180_degrees, J_rotated_270_degrees))


def check_S(i, j):
    S = 0
    S_rotated_90_degrees = 0

    if i + 2 < N and j + 1 < M:
        S = LST[i][j] + LST[i+1][j] + LST[i+1][j+1] + LST[i+2][j+1]  # └┐

    if 0 <= i - 1 and j + 2 < M:                                                          # ┌
        S_rotated_90_degrees = LST[i][j] + LST[i][j+1] + LST[i-1][j+1] + LST[i-1][j+2]    # ┘

    return(max(S, S_rotated_90_degrees))


def check_Z(i, j):
    Z = 0
    Z_rotated_90_degrees = 0

    if i + 1 < N and j + 2 < M:
        Z = LST[i][j] + LST[i][j+1] + LST[i+1][j+1] + LST[i+1][j+2]    # ┐
                                                                       # └
    if 0 <= i - 2 and j + 1 < M:
        Z_rotated_90_degrees = LST[i][j] + LST[i-1][j] + LST[i-1][j+1] + LST[i-2][j+1]  # ┌┘

    return(max(Z, Z_rotated_90_degrees))


N, M = map(int, input().split())
LST = [list(map(int, input().split())) for _ in range(N)]

max_value = 0

for i in range(N):
    for j in range(M):
        num_I = check_I(i, j)
        num_O = check_O(i, j)
        num_T = check_T(i, j)
        num_L = check_L(i, j)
        num_J = check_J(i, j)
        num_S = check_S(i, j)
        num_Z = check_Z(i, j)
        max_value = max(max_value, num_I, num_O, num_T, num_L, num_J, num_S, num_Z)

print(max_value)