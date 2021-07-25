"""
*    author:  kattsun
*    created: 24-07-2021 20:57:50
"""

def main():
    S1 = input().strip()
    S2 = input().strip()
    S3 = input().strip()
    S4 = input().strip()
    S = {'H' , '2B' , '3B' , 'HR'}
    if len(S) == len({S1,S2,S3,S4}):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()