"""
*    author:  kattsun
*    created: 05-02-2021 20:27:02
"""

def main():
    n = int(input())
    s = set()

    for i in range(n):
        a = int(input())
        if a in s:
            s.remove(a)
        else:
            s.add(a)

    print(len(s))

if __name__ == '__main__':
    main()