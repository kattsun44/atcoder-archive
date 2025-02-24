import math
def main():
    x1, y1, x2, y2 = list(map(int, input().split(' ')))
    x = x2
    y = y2
    dx = x2 - x1
    dy = y2 - y1
    ans = ''

    for i in range(2):
        dx, dy = dy, dx
        dx = -dx
        x += dx
        y += dy
        ans += str(x) + ' '
        ans += str(y) + ' '
    
    print(ans)


if __name__ == '__main__':
    main()