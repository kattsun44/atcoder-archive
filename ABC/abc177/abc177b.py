def main():
    s = input()
    t = input()
    cnt = 0
    rep = len(t)
    

    for i in range(len(s) - len(t) + 1):
        comp = s[i:i + len(t)]
        for j in range(len(t)):
            if comp[j] != t[j]:
                cnt += 1
        if rep > cnt:
            rep = cnt
        cnt = 0
    print(rep)


if __name__ == '__main__':
    main()