"""
*    author:  kattsun
*    created: 06-03-2021 21:03:58
"""

def main():
    n = int(input())
    ans = 100000000
    la = []
    lb = []
    
    for i in range(n):
        a,b = map(int, input().split())
        la.append(a)
        lb.append(b)

    
    for i in range(n):
        for j in range(n):
            if i == j:
                ttl = la[i] + lb[j]
            else:
                ttl = max(la[i],lb[j])
            ans = min(ttl, ans)
    
    print(ans)
    

if __name__ == '__main__':
    main()