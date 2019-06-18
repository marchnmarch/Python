import requests

def getBitfinex():
    bitfinex = requests.get("https://api.bitfinex.com/v1/pubticker/btcusd")
    dataBitfinex = bitfinex.json()
    best_bid_Bi=dataBitfinex['bid']
    best_ask_Bi=dataBitfinex['ask']
    return float(best_bid_Bi), float(best_ask_Bi)

def getFromBitBay():
    bitBay = requests.get("https://bitbay.net/API/Public/BTC/ticker.json")
    dataBitBay = bitBay.json()
    best_bid_BB=dataBitBay['bid']
    best_ask_BB=dataBitBay['ask']
    return best_bid_BB, best_ask_BB

Bitfinex = getBitfinex()
BitBay = getFromBitBay()

if Bitfinex[0] > BitBay[0] and Bitfinex[1] > BitBay[1]:
    print('Bitfinex bid: {}  ask: {}'.format(Bitfinex[0],Bitfinex[1]))
    print('BitBay bid:   {} ask: {}'.format(BitBay[0], BitBay[1]))
    print("1. Currently the BitBay exchange market is better for buying whilst Bitfinex is better for selling.")

elif Bitfinex[0] > BitBay[0] and Bitfinex[1] < BitBay[1]:
    print('Bitfinex bid: {}  ask: {}'.format(Bitfinex[0], Bitfinex[1]))
    print('BitBay bid:   {} ask: {}'.format(BitBay[0], BitBay[1]))
    print("2. Currently the Bitfinex exchange market is better for buying whilst Bitfinex is better for selling.")

elif Bitfinex[0] < BitBay[0] and Bitfinex[1] > BitBay[1]:
    print('Bitfinex bid: {}  ask: {}'.format(Bitfinex[0], Bitfinex[1]))
    print('BitBay bid:   {} ask: {}'.format(BitBay[0], BitBay[1]))
    print("3. Currently the BitBay exchange market is better for buying whilst BitBay is better for selling.")

elif Bitfinex[0] < BitBay[0] and Bitfinex[1] < BitBay[1]:
    print('Bitfinex bid: {}  ask: {}'.format(Bitfinex[0], Bitfinex[1]))
    print('BitBay bid:   {} ask: {}'.format(BitBay[0], BitBay[1]))
    print("4.Currently the Bitfinex exchange market is better for buying whilst BitBay is better for selling.")


