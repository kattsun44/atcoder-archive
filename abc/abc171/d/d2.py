"""
*    author:  kattsun
*    created: 11-02-2021 19:03:48
"""

def main():
    n = int(input())
    a = list(map(int, input().split()))
    num = [0] * 10000000
    sum = 0

    for i in range(n):
        num[a[i]] += 1
        sum += a[i]

    q = int(input())

    for i in range(q):
        b,c = map(int, input().split())
        num[c] += num[b]
        sum += c * num[b]
        sum -= b * num[b]
        num[b] = 0
        print(sum)

if __name__ == '__main__':
    main()