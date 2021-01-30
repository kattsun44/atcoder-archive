def main():
    n = input().strip()
    n = list(n)
    e = list(set(n))
    d = dict(zip(e, [0, 0, 0, 0]))
    cnt = 0

    for i in n:
        d[i] += 1

    ans = 'Yes' if len(e) == 2 and d[e[0]] == d[e[1]] else 'No'
    print(ans)

    

if __name__ == '__main__':
    main()