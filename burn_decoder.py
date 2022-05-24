import json
import warnings
from web3 import Web3
from config import PROVIDER,BURN_CONTRACT_ADDRESS,BURN_ABI_PATH

warnings.filterwarnings("ignore")
web3 = Web3(Web3.HTTPProvider(PROVIDER))

def decode_burnevent(receipt):
    """
    Function for decoding burn event
    Accepting transaction receipt as parameter
    """
    # Reading ABI that have Burn event
    with open(BURN_ABI_PATH, 'r') as abi_config:
        burn_abi = json.load(abi_config)
    burn_contract = web3.eth.contract(address=BURN_CONTRACT_ADDRESS, abi=burn_abi)
    decoded_event=burn_contract.events.Burner().processReceipt(receipt)
    for burn_event in decoded_event:
        print(
            "----------------Burn Event------------------",
            "\nevent: ", burn_event['event'],
            "\nvalue: ", burn_event['args']['value'],
            "\nlogIndex: ", burn_event['logIndex'],
            "\ntransactionIndex: ", burn_event['transactionIndex'],
            "\ntransactionHash: ", burn_event['transactionHash'].hex(),
            "\naddress: ", burn_event['address'],
            "\nblockHash: ", burn_event['blockHash'].hex(),
            "\nblockNumber: ", burn_event['blockNumber']
        )



