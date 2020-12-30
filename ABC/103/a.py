def main():
    a1, a2, a3 = list(map(int, input().split(' ')))
    A = [a1, a2, a3]
    A.sort()
    t = 0

    for i in range(2):
        t += abs(A[i + 1] - A[i])
    print(t)

if __name__ == '__main__':
    main()