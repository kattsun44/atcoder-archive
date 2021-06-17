"""
*    author:  kattsun
*    created: 18-06-2021 07:05:36
"""

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append((x, i))
        Y.append((y, i))
    X2 = sorted(X, key=lambda x:x[0])
    Y2 = sorted(Y, key=lambda x:x[0])
    d = []
    d.append((abs(X2[-1][0]-X2[0][0]), str(X2[-1][1]) +'-'+ str(X2[0][1])))
    d.append((abs(X2[-1][0]-X2[1][0]), str(X2[-1][1]) +'-'+ str(X2[1][1])))
    d.append((abs(X2[-2][0]-X2[0][0]), str(X2[-2][1]) +'-'+ str(X2[0][1])))
    d.append((abs(X2[-2][0]-X2[1][0]), str(X2[-2][1]) +'-'+ str(X2[1][1])))
    d.append((abs(Y2[-1][0]-Y2[0][0]), str(Y2[-1][1]) +'-'+ str(Y2[0][1])))
    d.append((abs(Y2[-1][0]-Y2[1][0]), str(Y2[-1][1]) +'-'+ str(Y2[1][1])))
    d.append((abs(Y2[-2][0]-Y2[0][0]), str(Y2[-2][1]) +'-'+ str(Y2[0][1])))
    d.append((abs(Y2[-2][0]-Y2[1][0]), str(Y2[-2][1]) +'-'+ str(Y2[1][1])))
    d = sorted(d,key=lambda x:x[0], reverse=True)
    # 家が重複しているか
    if d[1][1] == d[2][1]:
        print(d[2][0])
    else:
        print(d[1][0])

if __name__ == '__main__':
    main()