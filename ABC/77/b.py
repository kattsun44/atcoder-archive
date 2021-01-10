import math
def main():
    n = int(input())

    for i in range(n):
        if math.sqrt(n - i) == math.floor(math.sqrt(n - i)):
            print(n - i)
            return
    
if __name__ == '__main__':
    main()