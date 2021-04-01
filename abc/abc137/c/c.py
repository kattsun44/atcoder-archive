"""
*    author:  kattsun
*    created: 01-02-2021 19:42:08
"""
from math import factorial
def main():
    n = int(input())
    words = {}
    for i in range(n):
        word = list(input().strip())
        word.sort()
        word = ",".join(word)
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    ans = 0
    for value in words.values():
        if value != 1:
            ans += int(factorial(value) / (factorial(2) * factorial(value - 2) ))
    print(ans)

if __name__ == '__main__':
    main()