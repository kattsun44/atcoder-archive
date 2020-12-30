def main():
    n = set(input().strip())
    s = set(['a', 'b', 'c'])
    ans = 'Yes' if n == s else 'No'
    print(ans)

if __name__ == '__main__':
    main()