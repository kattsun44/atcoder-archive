"""
*    author:  kattsun
*    created: 02-07-2021 07:38:36
"""

def main():
    N = int(input())
    user = set()
    for i in range(N):
        num = i + 1
        S = input().strip()
        if S in user:
            continue
        else:
            user.add(S)
            print(num)


if __name__ == '__main__':
    main()