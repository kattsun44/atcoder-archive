"""
*    author:  kattsun
*    created: 27-02-2021 22:06:19
"""

def main():
    k = int(input())
    s = input().strip()
    t = input().strip()
    sd = {1: 0,2: 0,3: 0,4: 0,5: 0,6: 0,7: 0,8: 0,9: 0}
    td = {1: 0,2: 0,3: 0,4: 0,5: 0,6: 0,7: 0,8: 0,9: 0}
    sp,tp = (0,0)
    for i in range(4):
        c = int(s[i])
        if c in sd:
            sd[c] += 1
        else:
            sd[c] = 1
    for i in range(4):
        c = int(t[i])
        if c in td:
            td[c] += 1
        else:
            td[c] = 1
    print(sd,td)
    for i in range(9):
        c = 9-i
        if c in sd:
            sd[c] += 1
            if sd[c] > k:
                continue
        else:
            sc[c] == 1
        for k,v in sd.items():
            sp += k * 10 ** v
        for j in range(9):
            ct = 9-j
            if c in td and td:
                td[ct] += 1
                if td[ct] > k:
                    continue
            else:
                sc[c] == 1
            for k,v in td.items():
                tp += k * 10 ** v
    
    print(sp,tp)
    bunbo = k * 9 - 4
        c = 9 - i
        if sp + 



if __name__ == '__main__':
    main()