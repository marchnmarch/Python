import requests
from random import random, randint
from time import sleep

def getFromBitBay():
    bitBay = requests.get("https://bitbay.net/API/Public/BTC/ticker.json")
    dataBitBay = bitBay.json()
    bestBid_BB=dataBitBay['bid']
    bestAsk_BB=dataBitBay['ask']
    return bestBid_BB, bestAsk_BB

listOfUsers = []
listOfWallets = []


numberOfUsers = 50 #100
transactionPerMinute = 100
allTransactionAmount = 100

for i in range(numberOfUsers):
    users = requests.get("https://randomuser.me/api/")
    dataUsers = users.json()
    firstName = dataUsers['results'][0]['name']['first']
    lastName = dataUsers['results'][0]['name']['last']
    ID = dataUsers['results'][0]['login']['uuid']
    listOfUsers.append([i+1, firstName, lastName])
    listOfWallets.append([ID, random()*10000, random()])


BTCUSD, USDBTC = getFromBitBay()

currentTransactionAmount = 0

while(currentTransactionAmount != allTransactionAmount):
    firstUserIndex = randint(0, numberOfUsers - 1)
    secondUserIndex = randint(0, numberOfUsers - 1)
    while listOfWallets[firstUserIndex][0] == listOfWallets[secondUserIndex][0]:
        secondUserIndex = randint(0, numberOfUsers - 1)
    amountBTC = random() / 10
    if amountBTC < listOfWallets[firstUserIndex][2] and amountBTC*USDBTC < listOfWallets[secondUserIndex][1]:
        print("User {} {} exchanged {} BTC with user {} {} for {} USD.".format(listOfUsers[firstUserIndex][1], listOfUsers[firstUserIndex][2], amountBTC, listOfUsers[secondUserIndex][1], listOfUsers[secondUserIndex][2], amountBTC * USDBTC))
        listOfWallets[firstUserIndex][2] -= amountBTC
        listOfWallets[secondUserIndex][2] += amountBTC
        listOfWallets[firstUserIndex][1] += amountBTC*BTCUSD
        listOfWallets[secondUserIndex][1] -= amountBTC*USDBTC

    elif amountBTC < listOfWallets[secondUserIndex][2] and amountBTC*USDBTC < listOfWallets[firstUserIndex][1]:
        print("User {} {} exchanged {} BTC with user {} {} for {} USD.".format(listOfUsers[secondUserIndex][1], listOfUsers[secondUserIndex][2], amountBTC, listOfUsers[firstUserIndex][1], listOfUsers[firstUserIndex][2], amountBTC * USDBTC))
        listOfWallets[secondUserIndex][2] -= amountBTC
        listOfWallets[firstUserIndex][2] += amountBTC
        listOfWallets[secondUserIndex][1] += amountBTC * BTCUSD
        listOfWallets[firstUserIndex][1] -= amountBTC * USDBTC

    else:
        print("Transaction impossible to execute.")
    sleep(60 / transactionPerMinute)
    currentTransactionAmount += 1

