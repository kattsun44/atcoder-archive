import math
def main():
    s = input().strip()
    hl = math.floor(len(s) / 2)
    fh = list(s[:hl])
    lh = list(s[-hl:])
    lh.reverse()
    cnt = 0

    for i in range(hl):
        if fh[i] != lh[i]:
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()