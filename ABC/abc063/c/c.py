"""
*    author:  kattsun
*    created: 18-02-2021 08:05:18
"""

def main():
    n = int(input())
    s1 = []
    s10 = []
    for _ in range(n):
        s = int(input())
        if s % 10 == 0:
            s10.append(s)
        else:
            s1.append(s)
    
    s1.sort()
    s10.sort()

    while (sum(s1)+sum(s10)) % 10 == 0:
        if len(s1) > 0:
            s1.pop(0)
        else:
            print(0)
            return

    print(sum(s1)+sum(s10))

if __name__ == '__main__':
    main()