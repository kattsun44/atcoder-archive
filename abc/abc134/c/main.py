"""
*    author:  kattsun
*    created: 06-06-2021 11:48:34
"""


def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    sorted_A = sorted(A)
    largest = max(A)
    second_largest = sorted_A[-2]
    for i in range(N):
        if A[i] == largest:
            print(second_largest)
        else:
            print(largest)


if __name__ == '__main__':
    main()
