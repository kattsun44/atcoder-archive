"""
*    author:  kattsun
*    created: 20-11-2021 11:58:20
"""
import itertools


def main():
    N = int(input())
    cnts = [0, 0, 0, 0, 0]
    for i in range(N):
        S = input().strip()
        if S[0] == 'M':
            cnts[0] += 1
        elif S[0] == 'A':
            cnts[1] += 1
        elif S[0] == 'R':
            cnts[2] += 1
        elif S[0] == 'C':
            cnts[3] += 1
        elif S[0] == 'H':
            cnts[4] += 1

    c = itertools.combinations(cnts, 3)
    ans = 0
    for v in c:
        ans += v[0] * v[1] * v[2]
    print(ans)


if __name__ == '__main__':
    main()
