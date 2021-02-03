"""
*    author:  kattsun
*    created: 03-02-2021 20:18:52
"""

def main():
    n = int(input())
    T = [0,0,0,0,0,0]
    for i in range(n):
        M,m = map(float, input().split())
        if m >= 25:
            T[3] += 1

        if M >= 35:
            T[0] += 1
        elif M >= 30:
            T[1] += 1
        elif M >= 25:
            T[2] += 1
        if M >= 0:
            if m < 0:
                T[4] += 1
        else:
            T[5] += 1
    
    print(str(T)[1:-1].replace(',', ''))

if __name__ == '__main__':
    main()