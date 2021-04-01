def main():
    n = int(input())
    dict = {'AC':0, 'WA':0, 'TLE':0, 'RE':0}
    for i in range(n):

        dict[input()] += 1

    print('AC', 'x', dict['AC'])
    print('WA', 'x', dict['WA'])
    print('TLE', 'x', dict['TLE'])
    print('RE', 'x', dict['RE'])

if __name__ == '__main__':
    main()