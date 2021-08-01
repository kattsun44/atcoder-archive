"""
*    author:  kattsun
*    created: 31-07-2021 21:54:47
"""
from collections import deque


def main():
    Q = int(input())
    bag = deque()
    cnt = 0
    flag = False
    for _ in range(Q):
        S = input().strip()
        n = int(S[0])
        if len(S) != 1:
            x = int(S.split(' ')[-1])

        if n == 1:
            if flag:
                if x <= bag[0] + cnt:
                    bag.appendleft(x)
                else:
                    bag.append(x)
            else:
                bag.append(x)
            flag = True
        elif n == 2 and len(bag):
            cnt += x
        else:
            print(bag.popleft() + cnt)
            if len(bag) == 0:
                cnt = 0


if __name__ == '__main__':
    main()
