def main():
    x = list(map(int, input().split(' ')))
    sx, sy, gx, gy = x
    ans = sx + (gx - sx) * sy / (sy + gy)
    print(ans)

if __name__ == '__main__':
    main()