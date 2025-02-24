def main():
    x = int(input())
    L = [1]

    for i in range(x):
        for j in range(x):
            if i != 0:
                a = (i + 1) ** (j + 2)
                if a > x:
                    break
                L.append(a)
    
    print(max(L))


if __name__ == '__main__':
    main()