"""
*    author:  kattsun
*    created: 31-05-2021 07:33:01
"""
from collections import deque

def main():
    S = deque(input().strip())
    Q = int(input())
    rv = 0
    for i in range(Q):
        q = list(input().split())
        t = int(q[0])
        if t == 1:
            rv += 1
        if t == 2:
            f = int(q[1])
            c = q[2]
            if rv % 2 == 0:
                if f == 1:
                    S.appendleft(c)
                else:
                    S.append(c)
            else:
                if f == 1:
                    S.append(c)
                else:
                    S.appendleft(c)
    if rv % 2 ==1:
        S = ''.join(list(reversed(S)))
    else:
        S = ''.join(S)
    print(S)
        

if __name__ == '__main__':
    main()