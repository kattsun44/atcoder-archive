"""
*    author:  kattsun
*    created: 02-02-2021 20:23:52
"""
import itertools
def main():
    nums = list(map(int, input().split()))
    sums = []
    for i in itertools.combinations(nums, 3):
        sums.append(sum(i))
    sums.remove(max(sums))
    sums.remove(max(sums))
    print(max(sums))

if __name__ == '__main__':
    main()