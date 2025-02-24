"""
*    author:  kattsun
*    created: 20-08-2021 21:41:56
"""


def main():
    a, b = map(str, input().split())
    if a == "H":
        if b == "H":
            print("H")
        else:
            print("D")
    else:
        if b == "H":
            print("D")
        else:
            print("H")


if __name__ == '__main__':
    main()
