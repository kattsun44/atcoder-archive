"""
*    author:  kattsun
*    created: 30-04-2021 11:51:28
"""


def main():
    S = input().strip()
    for i in range(len(S)//2):
        S = S[:-2]
        if S[:len(S)//2] == S[len(S)//2:]:
            print(len(S))
            return


if __name__ == '__main__':
    main()
