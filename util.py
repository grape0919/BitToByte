
def earn(buy, sell):
    return ((sell-buy)/buy)*100

if __name__ == '__main__':
    print(earn(1556,1583))