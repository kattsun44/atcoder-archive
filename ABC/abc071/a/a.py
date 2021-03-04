"""
*    author:  kattsun
*    created: 04-03-2021 12:11:55
"""
def main():
    x,a,b = map(int, input().split())
    l = ['A', 'B']
    d = [abs(x-a),abs(x-b)]
    print(l[d.index(min(d))])

if __name__ == '__main__':
    main()
