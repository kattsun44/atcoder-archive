def main():
    n = int(input())
    t = sum(list(map(int, list(str(n)))))
    jdg = 'Yes' if n % t == 0 else 'No'
    print(jdg)

if __name__ == '__main__':
    main()