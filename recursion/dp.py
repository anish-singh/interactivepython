


def findMinCoins(change, cList) :
    
    if change in cList: 
        return 1
    
    minCoins = change
    for c in cList:
        if c > change: continue
        n = findMinCoins(change -c, cList)
        if n < minCoins: minCoins = n
    return minCoins + 1


minMap = {}
def findMinCoinsWithCaching(change, cList):
    
    if change in minMap: return minMap[change]
    
    if change in cList: 
        minMap[change]=1
        return 1
    
    minCoins = change
    for c in cList:
        if c > change: continue
        n = findMinCoins(change -c, cList)
        if n < minCoins: minCoins = n
    minMap[change] = minCoins + 1
    return minCoins + 1



def findMinCoinsWithDP(change, coinList):
    
    minList = [0] * (change +1)
    lastCoinUsed = [0] * (change +1)
    for i in [x for x in coinList if x <= change]: 
        minList[i] = 1
        lastCoinUsed[i] = i
    
    pos = 1
    for pos in range(1,change+1):
        minValue = change
        for c in [x for x in coinList if x <= pos]:
            if minList[pos-c] < minValue:
                minvalue = minList[pos-c]
                lastCoinUsed[pos] = c
        minList[pos] = minvalue + 1
    print minList
    printCoinsUsed(change, lastCoinUsed)
    
    
def printCoinsUsed(change, coinsUsed):
    while change > 0:
        print coinsUsed[change]
        change = change - coinsUsed[change]
    
                

    
def main():
    #print findMinCoins(63, [1,5,10,25])
    #print findMinCoinsWithDP(63, [1,5,10,25], [0]*63)
    print findMinCoinsWithDP(13, [1,5,10,25])
    
    
if __name__ == '__main__':
    main()