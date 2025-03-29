import os
import json
import datetime


#def parseTickers(file, symbol, security, marketCategory):
def parseTickers(filename):

    try:
        DIR_PATH = os.path.dirname(os.path.realpath(__file__))
        DIR_PATH = os.path.join(DIR_PATH, "..", "data")
    except NameError:
        DIR_PATH = os.getcwd()

    tickers = []

    # TODO: async otherlisted.txt?
    #with open("nasdaqlisted.txt", "r") as file:
    #with open(filename, "r") as file:
    with open(f"{DIR_PATH}/{filename}", "r") as file:
        content = file.read().splitlines()
        header = content[0].split("|")
        date = content[-1].split("|")[0][:]
        date = date[len("File Creation Time: "):]
        date = datetime.datetime.strptime(date, "%m%d%Y%H:%M")
        content = content[1:-1]
        for c in content:
            [Symbol, Security_Name, Market_Category, Test_Issue, Financial_Status, Round_Lot_Size, ETF, NextShares] = c.split("|")
            if (Test_Issue == "N" and (Financial_Status == "N" or Financial_Status == "D" or Financial_Status == "E" or Financial_Status == "H")):
                tickers.append(Symbol)
                # TODO: more filtering options below...
                #if "common stock" in Security_Name.lower():
                #if "depositary" in Security_Name.lower():
                #if "warrant" in Security_Name.lower():
                #if Market_Category == "Q" "G" "S"

    """
    A = NYSE MKT
    N = New York Stock Exchange (NYSE)
    P = NYSE ARCA
    Z = BATS Global Markets (BATS)
    V = Investors' Exchange, LLC (IEXG)
    """
    print(len(tickers))
    print(len(list(set(tickers))))

    #with open("otherlisted.txt", "r") as file:
    with open(f"{DIR_PATH}/otherlisted.txt", "r") as file:
        content = file.read().splitlines()
        header = content[0].split("|")
        date = content[-1].split("|")[0][:]
        date = date[len("File Creation Time: "):]
        date = datetime.datetime.strptime(date, "%m%d%Y%H:%M")
        content = content[1:-1]

        for c in content:
            [ACT_Symbol, Security_Name, Exchange, CQS_Symbol, ETF, Round_Lot_Size, Test_Issue, NASDAQ_Symbol] = c.split("|")
            if (Test_Issue == "N" and ACT_Symbol == CQS_Symbol == NASDAQ_Symbol and (Exchange == "A" or Exchange == "N" or Exchange == "P")):
                tickers.append(NASDAQ_Symbol)
                # TODO: more filtering options below...
                #if "common stock" in Security_Name.lower():
                #if "depositary" in Security_Name.lower():
                #if "warrant" in Security_Name.lower():


    print(len(tickers))
    print(len(list(set(tickers))))

    with open(f"{DIR_PATH}/tickers.json", "w+") as file:
        json.dump(tickers, file)



if __name__ == "__main__":
    parseTickers("nasdaqlisted.txt")
   #parseTickers("nasdaqlisted.txt", exchanges="ANP") # NYSE, 