def main():
    s = int(input())
    L = []
    cnt = 1

    while True:
        cnt += 1
        L.append(s)
        if s % 2 == 0:
            s = s / 2
        else:
            s = s * 3 + 1
        if s in L:
            break
        pass
    print(cnt)

if __name__ == '__main__':
    main()