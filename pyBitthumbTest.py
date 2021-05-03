import pybithumb
from reprint import output
import time
import util

NUM_OUTPUT_COLOMN = 4
INTERVAL = "hour"
tickers = pybithumb.get_tickers()
# print(tickers)
all = {}

def bull_market(ticker, interval):
    df = pybithumb.get_ohlcv(ticker,interval=INTERVAL)
    if not df is None:
        ma = df['close'].rolling(window=interval).mean()
        time.sleep(0.1)
        print("1", ma[-1])
        print("2", ma[-2])
        return ma[-1]
    else :
        print("failed make bull : ", interval)

def make_bull_matrix(interval):
    print("!@#!@# make ma5")
    write_str = ''
    if tickers:
        for ticker in tickers:
            print("make bull for [", ticker,"]")
            ma = bull_market(ticker,interval)
            write_str = write_str + ticker + "\t" + str(ma) + "\n"

        with open("ma"+str(interval),"w", encoding="utf8") as wf:
            wf.write(write_str)
            wf.close()
    else :
        print("Failed make bull metrix")

def process(threshold=3.0, interval=30):

    ma5_list = {}
    ma30_list = {}
    with open("ma5", "r", encoding="utf8") as rf:
        for line in rf.readlines():
            tup = line.split("\t")
            if tup[1] == 'None\n':
                tup[1] = 0.0
            ma5_list.update({tup[0]:float(tup[1])})
        rf.close()
    with open("ma30", "r", encoding="utf8") as rf:   
        for line in rf.readlines():
            tup = line.split("\t")
            if tup[1] == 'None\n':
                tup[1] = 0.0
            ma30_list.update({tup[0]:float(tup[1])})
        rf.close()


    with output(initial_len=int(len(tickers)/NUM_OUTPUT_COLOMN), interval=0) as output_line:
        while True:
            all = pybithumb.get_current_price("ALL")

            if all:
                print_str = ''

                i = 0
                for ticker, data in all.items() :
                    space = ''
                    check_value = round((ma30_list[ticker]-(float(data['closing_price'])))/float(data['closing_price'])*100,2)
                    for len_nm in range(30-((len(data['closing_price'])*3)+(len(ticker)))):
                        space = space + ' '
                    print_str = print_str + ('\033[33m' + f"({check_value}%)"\
                         if check_value > threshold and ma5_list[ticker] < ma30_list[ticker] and ma30_list[ticker] > float(data['closing_price']) else '\033[37m') + ticker \
                        + "\033[0m"
                    print_str = print_str + ' : ' + ('\033[31m' if float(data['closing_price']) >= float(data['opening_price']) else '\033[34m')  \
                        + data['closing_price'] + "\033[37m"
                    print_str = print_str + ' : ' + '\033[93m' + str(round(ma5_list[ticker],1)) + '\033[0m' + ' : ' + '\033[95m' + str(round(ma30_list[ticker],1)) + '\033[0m' + space
                    
                    if i % NUM_OUTPUT_COLOMN == 3:
                        line = int(i/NUM_OUTPUT_COLOMN)
                        # print( line )
                        output_line[line] = print_str
                        print_str = ''


                    i = i + 1
                # print(print_str, end='\r', flush=True)
                    

            time.sleep(15)

if __name__ == "__main__":
    # make_bull_matrix(5)
    # make_bull_matrix(30)
    process(threshold=3.0, interval=15)
    # hme()
