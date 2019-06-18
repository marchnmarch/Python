import requests
from random import random
from time import sleep
import secrets

def getFromBitBay():
    bitBay = requests.get("https://bitbay.net/API/Public/BTC/ticker.json")
    dataBitBay = bitBay.json()
    bestBid_BB=dataBitBay['bid']
    bestAsk_BB=dataBitBay['ask']
    return bestBid_BB, bestAsk_BB


listOfWallets = []


numberOfUsers = 50 #100
transactionPerMinute = 100
allTransactionAmount = 100

for i in range(numberOfUsers):
    users = requests.get("https://randomuser.me/api/")
    dataUsers = users.json()
    # firstName = dataUsers['results'][0]['name']['first']
    # lastName = dataUsers['results'][0]['name']['last']
    ID = dataUsers['results'][0]['login']['uuid']
    listOfWallets.append([ID, random()*10000, random()])


BTCUSD, USDBTC = getFromBitBay()


#secure = random.SystemRandom()

TransactionAmount = 0

while(TransactionAmount < allTransactionAmount):
    firstUserIndex = (secrets.choice(listOfWallets))
    secondUserIndex = (secrets.choice(listOfWallets))
    while firstUserIndex[0] == secondUserIndex[0]:
        secondUserIndex[0] = (secrets.choice(listOfWallets))
    amountBTC = random() / 10
    if amountBTC < firstUserIndex[2] and amountBTC*USDBTC < secondUserIndex[1]:
        print("User with ID:{} exchanged {} BTC with user with ID:{} for {} USD.".format(firstUserIndex[0], amountBTC, secondUserIndex[0], amountBTC * USDBTC))
        firstUserIndex[2] -= amountBTC
        secondUserIndex[2] += amountBTC
        firstUserIndex[1] += amountBTC*BTCUSD
        secondUserIndex[1] -= amountBTC*USDBTC

    elif amountBTC < secondUserIndex[2] and amountBTC*USDBTC < firstUserIndex[1]:
        print("User with ID:{} exchanged {} BTC with user with ID:{} for {} USD.".format(secondUserIndex[0], amountBTC, firstUserIndex[0], amountBTC * USDBTC))
        secondUserIndex[2] -= amountBTC
        firstUserIndex[2] += amountBTC
        secondUserIndex[1] += amountBTC*BTCUSD
        firstUserIndex[1] -= amountBTC*USDBTC

    else:
        print("Transaction impossible to execute.")
    sleep(60 / transactionPerMinute)
    TransactionAmount += 1