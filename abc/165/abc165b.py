import math
def main():
    x = int(input())
    m = 100
    cnt = 0

    while m < x:
        m += math.floor(m / 100)
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()