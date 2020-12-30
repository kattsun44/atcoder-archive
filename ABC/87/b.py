def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    t = 0
    cnt = 0

    for i in range(a + 1):
        t += 500 * i
        for j in range(b + 1):
            t += 100 * j
            for k in range(c + 1):
                t += 50 * k
                if t == x:
                    cnt += 1
                t -= 50 * k
            t -= 100 * j
        t -= 500 * i
    
    print(cnt)

if __name__ == '__main__':
    main()