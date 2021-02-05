"""
*    author:  kattsun
*    created: 05-02-2021 20:35:05
"""

def main():
    n = int(input())
    r = input().strip()
    cnt = 0

    for i in range(n):
        if r[i] == 'A':
            cnt += 4
        elif r[i] == 'B':
            cnt += 3
        elif r[i] == 'C':
            cnt += 2
        elif r[i] == 'D':
            cnt += 1            
    
    gpa = 0 if cnt == 0 else cnt / n
    print(gpa)

if __name__ == '__main__':
    main()