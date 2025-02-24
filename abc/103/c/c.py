"""
*    author:  kattsun
*    created: 05-02-2021 20:52:42
"""

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_sum = sum(a)
    
    print(a_sum - n)

if __name__ == '__main__':
    main()