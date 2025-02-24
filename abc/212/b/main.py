"""
*    author:  kattsun
*    created: 31-07-2021 20:53:47
"""


def main():
    S = input().strip()
    is_same = False
    if len(set(S)) == 1:
        print('Weak')
        return
    cnt = 0
    for i in range(3):
        if (int(S[i]) + 1) % 10 == int(S[i+1]):
            cnt += 1
    if cnt == 3:
        print('Weak')
    else:
        print('Strong')


if __name__ == '__main__':
    main()
