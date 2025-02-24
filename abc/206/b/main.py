"""
*    author:  kattsun
*    created: 19-06-2021 21:02:36
"""


def main():
    N = int(input())
    ttl = 0
    for i in range(1, 1000000001):
        ttl += i
        if ttl >= N:
            print(i)
            return


if __name__ == '__main__':
    main()
