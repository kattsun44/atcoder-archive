import math
def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    L = [a, b, c, d, e]
    S = []
    t = 0

    for i in range(5):
        for j in range(5):
            m = math.ceil(L[j] / 10) * 10
            t += m
        t -= (math.ceil(L[i] / 10) * 10 - L[i])
        S.append(t)
        t = 0

    
    print(min(S))

if __name__ == '__main__':
    main()