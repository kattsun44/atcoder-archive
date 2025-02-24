"""
*    author:  kattsun
*    created: 09-02-2021 16:58:41
"""
def main():
    a = int(input())
    b = int(input())
    n = int(input())
    ans = n
    while True:
        if ans % a == 0 and ans % b == 0:
            print(ans)
            return
        ans += 1

if __name__ == '__main__':
    main()