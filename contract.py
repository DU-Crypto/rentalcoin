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

def deploy(token:Token):
	if not CheckWitness(token.owner):
		print("You must be the owner to deploy")
		return False

	storage = StorageAPI()

	if not storage.get("init"):
		storage.put("init",1)
		storage.put(token.owner,token.initial_amount)
		token.addToTotalSupply(token.initial_amount,storage)
