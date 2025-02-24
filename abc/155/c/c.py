def main():
    n = int(input())
    d = dict()

    for i in range(n):
        key = input().strip()
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    
    # 登場回数が最多の単語のみのリスト
    mode_words = []
    mode_value = max(d.values())
    for i in d:
        if d[i] == mode_value:
            mode_words.append(i)

    mode_words = sorted(mode_words)

    for word in mode_words:
        print(word)

if __name__ == '__main__':
    main()