"""
*    author:  kattsun
*    created: 23-06-2021 08:11:19
"""

def main():
    N = int(input())
    for a in range(1, 101):
        for b in range(1, 101):
            if 3 **a + 5 ** b == N:
                print(a, b)
                return
    print(-1)

if __name__ == '__main__':
    main()