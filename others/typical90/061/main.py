"""
*    author:  kattsun
*    created: 04-07-2021 09:28:48
"""
from collections import deque


def main():
    Q = int(input())
    deck = deque()
    for i in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            deck.appendleft(x)
        elif t == 2:
            deck.append(x)
        else:
            print(deck[x-1])


if __name__ == '__main__':
    main()
