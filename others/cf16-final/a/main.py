"""
*    author:  kattsun
*    created: 05-07-2021 06:51:28
"""

def main():
    H, W = map(int, input().split())
    AtoZ = [chr(i) for i in range(65, 91)]
    for i in range(H):
        S = list(map(str, input().split()))
        for j, word in enumerate(S):
            if word == 'snuke':
                print(AtoZ[j] + str(i + 1))
                return

if __name__ == '__main__':
    main()