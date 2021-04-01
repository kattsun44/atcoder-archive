def main():
    n = input().strip()
    aa = int(n[:2])
    bb = int(n[2:])

    if aa == 0:
        if 1 <= bb <= 12:
            print('YYMM')
        else:
            print('NA')
    elif 1 <= aa <= 12:
        if 1 <= bb <= 12:
            print('AMBIGUOUS')
        else:
            print('MMYY')
    else:
        if 1 <= bb <= 12:
            print('YYMM')
        else:
            print('NA')
    
if __name__ == '__main__':
    main()