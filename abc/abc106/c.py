def main():
    S = list(map(int,list(input().strip())))
    K = int(input())
    t = 0
    
    for i in S:
        t += i ** 10000
        if t > K:
            print(i)
            return

if __name__ == '__main__':
    main()