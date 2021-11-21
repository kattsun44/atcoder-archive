"""
*    author:  kattsun
*    created: 21-11-2021 11:53:04
"""


def main():
    N = int(input())
    A = []
    for i in range(5):
        M = int(input())
        A.append(M)
    cnt = 4
    print(cnt + -(-N // min(A)))


if __name__ == '__main__':
    main()
