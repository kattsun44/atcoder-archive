def main():
    l = list(map(int, input().split(' ')))
    t = 0

    for i in range(2):
        t += max(l)
        l[l.index(max(l))] -= 1
    
    print(t)

if __name__ == '__main__':
    main()