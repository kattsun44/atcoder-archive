import numpy as np
def main():
    n, m = list(map(int, input().split(' ')))
    ks = list(range(1, m + 1))
    vs = np.zeros(m)
    d = dict(zip(ks, map(int, vs)))
    cnt = 0
    
    for i in range(n):
        A = list(map(int, input().split(' ')))[1:]
        for j in A:
            if j in d:
                d[j] += 1


    for i in d:
        if d[i] == n:
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()