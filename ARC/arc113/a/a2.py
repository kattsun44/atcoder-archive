"""
*    author:  kattsun
*    created: 21-02-2021 20:59:33
"""
def main():
    k = int(input())
    cnt = 0
    for i in range(k):
        for j in range(k-i):
            for l in range(k-i-j):
                abc = (i+1)*(j+1)*(l+1)
                if abc <= k:
                    cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()