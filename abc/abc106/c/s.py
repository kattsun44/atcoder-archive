"""
*    author:  kattsun
*    created: 30-04-2021 11:28:19
"""


def main():
    S = input().strip()
    K = int(input())
    for i in range(K):
        if S[i] != '1':
            print(int(S[i]))
            return
    print(1)


if __name__ == '__main__':
    main()
