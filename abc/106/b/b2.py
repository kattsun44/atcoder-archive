import math
def main():
    n = int(input())
    cnt = 0

    for i in range(math.ceil(n / 2)):
        o = i * 2 + 1
        div = 0
        for j in range(i):
            if o % (j + 1) == 0:
                div += 1
        if div == 7:
            cnt += 1
    
    print(cnt)

if __name__ == '__main__':
    main()