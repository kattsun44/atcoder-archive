"""
*    author:  kattsun
*    created: 23-01-2021 12:53:38
"""

def main():
    n,m = map(int, input().split(' '))
    record = dict()
    AC = 0
    pen = 0

    for i in range(m):
        p, s = input().split(' ')
        if p not in record:
            if s == 'WA' :
                record[p] = 1
            elif s == 'AC':
                AC += 1
                record[p] = 0
        elif record[p] != 0:
            if s == 'AC':
                pen += record[p]
                AC += 1
                record[p] = 0
            else:
                record[p] += 1
    
    print(AC, pen)

if __name__ == '__main__':
    main()