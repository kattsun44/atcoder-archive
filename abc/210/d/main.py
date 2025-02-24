"""
*    author:  kattsun
*    created: 17-07-2021 20:56:35
"""


def main():
    H, W, C = map(int, input().split())
    A = list(map(int, input().split()))
    b = []
    for i in range(H * 2 - 1):
        l = []
        for j in range(W * 2 - 1):
            a = abs(-(-(H - 1) // 2) - i + 1) + abs(-(-(W - 1) // 2) - j + 1)
            l.append(C * a)
        b.append(l)
    print(b)


if __name__ == "__main__":
    main()
