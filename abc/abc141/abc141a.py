def main():
    ws = ['Sunny', 'Cloudy', 'Rainy']
    s = input().strip()
    
    print(ws[(ws.index(s) + 1) % 3])

if __name__ == '__main__':
    main()