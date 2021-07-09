"""
*    author:  kattsun
*    created: 09-07-2021 08:37:52
"""
 
def main():
    N = int(input())
    ss = []
 
    # 文字数が奇数の場合は解無し
    if N % 2 == 1:
        print()
        return
    
    # Nをビット化し、'(' ')' を割り当てた文字列を作成
    for i in range(2**N):
        bin_i = str(bin(i)[2:]).zfill(N)
        s = ''
        for b in bin_i:
            if b == '0':
                s += '('
            else:
                s += ')'
        ss.append(s)
 
    for s in ss:
        # 括弧の累積和 ('('→1, ')'→-1 ), '(' の数、')'の数
        sum, sum0, sum1 = [0,0,0]
        sums = []
        for c in s:
            if c == '(':
                sum0 += 1
                sum += 1
            else:
                sum1 += 1
                sum -= 1
            sums.append(sum)
        # '(' ')' の数が異なる または 累積和がマイナスの場合、不適
        if sum0 != sum1 or min(sums) < 0:
            continue
        print(s)
 
 
if __name__ == '__main__':
    main()