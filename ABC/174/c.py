import math
def main():
    k = int(input())
    cnt = 0
    s = 0

    if k % 2 != 0 and k % 5 != 0:
        for i in range(999983):
            s += 10 ** i * 7
            cnt += 1
            if s >= k and s % k == 0:
                print(cnt)
                return
    else:
        print(-1)
        return

if __name__ == '__main__':
    main()