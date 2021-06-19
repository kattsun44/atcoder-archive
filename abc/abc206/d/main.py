"""
*    author:  kattsun
*    created: 19-06-2021 21:23:04
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))
    first = A[:N//2]
    last = A[-(-N//2):]
    last_reverse = list(reversed(last))
    S = set()
    for i in range(N//2):
        if first[i] == last_reverse[i]:
            continue
        else:
            S.add(first[i])
            S.add(last_reverse[i])
    print(max(len(S)-1, 0))


if __name__ == '__main__':
    main()
