import time

N = 8

board = [["." for _ in range(N)] for _ in range(N)]

def print_board():
    # header kolom
    print("  ", end="")
    for i in range(N):
        print(chr(97 + i), end=" ")
    print()

    # cetak papan (1 di bawah)
    for i in range(N - 1, -1, -1):
        print(i + 1, end=" ")
        for j in range(N):
            print(board[i][j], end=" ")
        print()

    print()
    time.sleep(0.5)

def is_safe(row, col):

    # cek kiri
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # diagonal kiri atas
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # diagonal kiri bawah
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == "Q":
            return False
        i += 1
        j -= 1

    return True


def solve(col):

    if col >= N:
        return True

    for i in range(N):

        posisi = f"{chr(97+col)}{i+1}"
        print(f"Mencoba queen di {posisi}")

        if is_safe(i, col):

            board[i][col] = "Q"
            print_board()

            if solve(col + 1):
                return True

            print("Backtracking...")
            board[i][col] = "."
            print_board()

    return False


if solve(0):
    print("Solusi ditemukan:")
    print_board()
else:
    print("Tidak ada solusi")
