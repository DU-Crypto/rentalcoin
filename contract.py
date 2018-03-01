from boa.blockchain.vm.Neo.Runtime import GetTrigger, CheckWitness, Notify
from boa.blockchain.vm.Neo.TriggerType import Application, Verification
from rentalcoin.token.token import Token
from rentalcoin.storage.storage import StorageAPI

def Main(op,args):
	token = new Token()
	storage = new StorageAPI()
	if op == 'deploy'
		return deploy(token)
	elif op == 'totalSupply'
		return token.getTotalSupply()
	elif op == 'name'
		return token.getName()
	elif op == 'symbol'
		return token.getSymbol()
	elif op == 'transfer'
		return token.transfer(args)
	elif op == 'balanceOf'
		return token.getBalanceOf(args)
	elif op == 'decimals'
		return token.getDecimals()
