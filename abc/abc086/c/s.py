"""
*    author:  kattsun
*    created: 20-04-2021 07:48:01
"""

def main():
    N = int(input())
    T, X, Y = 0, 0, 0 # 初期位置
    for i in range(N):
        t, x, y = map(int, input().split())
        time = t - T
        dist = abs(x - X) + abs(y - Y)
        if time % 2 == 0:
            if dist % 2 != 0 or time < dist:
                print('No')
                return
        elif time % 2 == 1:
            if dist % 2 != 1 or time < dist:
                print('No')
                return
        
        T, X, Y = t, x, y

    print('Yes')        

if __name__ == '__main__':
    main()