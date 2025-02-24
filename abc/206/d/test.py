def primeNumberCreate():
    primeList = [2]  # 2以下の素数リストを作成
    maxNumber = 1000000
    for x in range(3, maxNumber):
        for y in primeList:
            if x % y == 0:
                break
        else:
            primeList.append(x)  # 割り切れるものがなければリストに追加
    return primeList


def indentAdjustment(primeNumbers):  # インデント調節のため
    count = 0
    for num in primeNumbers:
        print(f"{num:4}", end=" ")
        count += 1
        if count > 9:
            print(' ')
            count = 0


if __name__ == '__main__':
    print(primeNumberCreate())
