def main():
    n = int(input())
    S = list(map(str.strip, input().split(' ')))
    s = len(set(S))

    jdg = 'Three' if s == 3 else 'Four'
    print(jdg)

if __name__ == '__main__':
    main()