"""
*    author:  kattsun
*    created: 19-04-2021 07:32:46
"""

def main():
    N = int(input())
    A = [0] * 10001

    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                f = x*x+y*y+z*z+x*y+y*z+z*x - 1
                if f <= N:
                    A[f] += 1
    
    for i in range(N):
        print(A[i])

if __name__ == '__main__':
    main()