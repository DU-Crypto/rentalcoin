from rentalcoin.storage.storage import StorageAPI

class Token():
    name = 'RentalCoin'
    symbol = 'RNC'
    total_supply = 10000000
    decimals = 8

    def getTotalSupply(self):
        return self.total_supply

    def getName(self):
        return self.name

    def getSymbol(self):
        return self.symbol

    def getDecimals(self):
        return self.decimals
        
