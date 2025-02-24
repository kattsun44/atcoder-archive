"""
*    author:  kattsun
*    created: 17-07-2021 21:07:47
"""


def main():
    N = int(input())
    S = input().strip()
    for i in range(N):
        if S[i] == "1":
            if i % 2 == 0:
                print("Takahashi")
            else:
                print("Aoki")
            return


if __name__ == "__main__":
    main()
