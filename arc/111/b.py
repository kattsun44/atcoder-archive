import math
def main():
    n = int(input())
    n = math.ceil(n / 111) * 111
    print(n)

if __name__ == '__main__':
    main()