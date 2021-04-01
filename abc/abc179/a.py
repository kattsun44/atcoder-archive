def main():
    x = input()
    if x[len(x) - 1] == 's':
        print(x + 'es')
    else:
        print(x + 's')

if __name__ == '__main__':
    main()