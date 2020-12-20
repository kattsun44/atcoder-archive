import statistics as stat

def main():
    nums = list(map(int, input().split(' ')))
    cnt = 0
    gcd = []

    for i in range(max(nums) - 1):
        for num in nums:
            if num % (i + 2) == 0:
                cnt+=1
                gcd.append(i + 2)
        cnt = 0
    print(stat.mode(gcd))

if __name__ == '__main__':
    main()