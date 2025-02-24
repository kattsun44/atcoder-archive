"""
*    author:  kattsun
*    created: 16-06-2021 09:34:13
"""


def main():
    A, B, C = map(int, input().split())
    parity_c = C % 2
    if parity_c == 0:
        parity_c += 2

    if B % 4 == 2 and parity_c == 1:
        if C == 1:
            bc_mod_4 = 2
        else:
            bc_mod_4 = 0
    else:
        bc_mod_4 = B ** parity_c % 4

    if bc_mod_4 == 0:
        bc_mod_4 += 4

    print(str(A ** bc_mod_4)[-1])


if __name__ == '__main__':
    main()
