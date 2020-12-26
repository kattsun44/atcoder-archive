import string
def main():
    C = input().strip()
    atoz = string.ascii_letters
    # atoz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
    #         'h', 'i', 'g', 'k', 'l', 'm', 'n', 
    #         'o', 'p', 'q', 'r', 's', 't', 'u',
    #         'v', 'w', 'x', 'y', 'z']
    
    print(atoz[atoz.index(C) + 1])

if __name__ == '__main__':
    main()