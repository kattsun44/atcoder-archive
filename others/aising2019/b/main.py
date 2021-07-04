"""
*    author:  kattsun
*    created: 04-07-2021 09:13:41
"""


def main():
    N = int(input())
    A, B = map(int, input().split())
    P = list(map(int, input().split()))
    P_by_point = [0] * 3
    for i in range(N):
        if P[i] <= A:
            P_by_point[0] += 1
        elif A+1 <= P[i] <= B:
            P_by_point[1] += 1
        else:
            P_by_point[2] += 1
    print(min(P_by_point))


if __name__ == '__main__':
    main()
