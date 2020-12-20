import math
def main():
    n = int(input())
    ps = list(map(int, input().split(' ')))
    m = sum(map(abs, ps))
    e = math.sqrt(sum(map(lambda x: x ** 2,ps)))
    c = max(map(abs, ps))
    print(m)
    print(e)
    print(c)

if __name__ == '__main__':
    main()