from rentalcoin.storage.storage import StorageAPI

class Token():
    name = 'RentalCoin'
    symbol = 'RNC'
    total_supply = 10000000
    decimals = 8
    storage = new StorageAPI()
    circulation_key = b'in_supply'
    # This is the script hash of the address for the owner of the token
    # This can be found in ``neo-python`` with the walet open, use ``wallet`` command
    owner = b'\xaf\x12\xa8h{\x14\x94\x8b\xc4\xa0\x08\x12\x8aU\nci[\xc1\xa5'

    def getTotalSupply(self):
        return storage.get(self.circulation_key)

    def addToTotalSupply(self,amount:int, storage:StorageAPI):
        current_supply = storage.get(self.circulation_key);
        current_supply += amount
        storage.put(self.circulation_key,current_supply)


    def getName(self):
        return self.name

    def getSymbol(self):
        return self.symbol

    def getDecimals(self):
        return self.decimals

    def getBalanceOf(args):
        account = args[0]
        return Storage.get(account)
    def transfer(args):
        from_account = args[0]
        to_account = args[1]
        amount = args[2]

        #check to see if the amount is less than or equal to zero
        if amount <= 0:
            print("Amount must be greater than zero")
            return False

        from_balance = storage.get(from_account)

        if from_balance < amount:
            print("Insufficient Funds!")
            return False
        to_balance = storage.get(to_account)

        new_from_balance = from_balance - amount
        new_to_balance = to_balance + amount

        storage.put(to_account,new_to_balance)
        storage.put(from_balance,new_from_balance)
        print("Transfer Complete")
        return True
