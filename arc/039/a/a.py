"""
*    author:  kattsun
*    created: 07-02-2021 09:34:28
"""

def main():
    a,b = map(int, input().split())
    a1 = int('9' + str(a)[1:])
    a2 = int(str(a)[0] + '9' + str(a)[-1])
    a3 = int(str(a)[:2] + '9')
    b1 = int('1' + str(b)[1:])
    b2 = int(str(b)[0] + '0' + str(b)[-1])
    b3 = int(str(b)[:2] + '0')
    
    print(max(max(a1,a2,a3) - b, a - min(b1,b2,b3)))

if __name__ == '__main__':
    main()