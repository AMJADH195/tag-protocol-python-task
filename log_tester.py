import json
import warnings
from web3 import Web3
from config import PROVIDER
from burn_decoder import decode_burnevent
from mint_decoder import decode_mintevent
from alloc_decoder import decode_allocevent


web3 = Web3(Web3.HTTPProvider(PROVIDER))
# Transaction hash of a purchase transaction on the given smart contract took from the bsc scan
transaction_hash='0x5992d254a6a815790681388083d71d1f94a8445bbab9a714259c3e1865077537'
receipt = web3.eth.getTransactionReceipt(transaction_hash)# Getting transaction receipt
decode_burnevent(receipt)# Call method for decoding Transaction Receipt mint event Logs
decode_mintevent(receipt)# Call method for decoding Transaction Receipt burn event Logs 
decode_allocevent(receipt)# Call method for decoding Transaction Receipt alloc event Logs