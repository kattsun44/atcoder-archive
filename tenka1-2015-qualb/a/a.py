"""
*    author:  kattsun
*    created: 12-02-2021 21:47:23
"""

def func(n):
    if n == 0: return 100
    if n == 1: return 100
    if n == 2: return 200
    return func(n-1) + func(n-2) + func(n-3)

def main():
    print(func(19))

if __name__ == '__main__':
    main()