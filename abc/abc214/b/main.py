"""
*    author:  kattsun
*    created: 18-11-2021 21:32:38
"""


def main():
    S, T = map(int, input().split())
    cnt = 0
    for a in range(S+1):
        for b in range(S-a+1):
            for c in range(S-(a+b)+1):
                if a*b*c <= T:
                    cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
