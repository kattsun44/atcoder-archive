"""
*    author:  kattsun
*    created: 24-05-2021 06:54:12
"""

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = dict()
    for i in range(N):
        if A[i] not in d:
            d[A[i]] = 1
        else:
            d[A[i]] += 1
    edges = []
    for k, v in d.items():
        if v >= 4:
            edges.append(k)
            edges.append(k)
        elif v >= 2:
            edges.append(k)
    edges.sort()
    if len(edges) >= 2:
        print(edges[-1] * edges[-2])
    else:
        print(0)

    

if __name__ == '__main__':
    main()