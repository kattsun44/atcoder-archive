def main():
    ws = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    s = input().strip()
    d = ws.index('SUN') - ws.index(s)
    ans = d if d != 0 else 7
    print(ans)

if __name__ == '__main__':
    main()