def main():
    n = input().strip()

    for i in range(len(n) - 1):
        if n[i] == n[i + 1]:
            print('Bad')
            return
    print('Good')

if __name__ == '__main__':
    main()