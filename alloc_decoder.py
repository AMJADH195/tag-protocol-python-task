import json
import warnings
from web3 import Web3
from config import PROVIDER, CONTRACT_ADDRESS, ABI_PATH

warnings.filterwarnings("ignore")
web3 = Web3(Web3.HTTPProvider(PROVIDER))


def decode_allocevent(receipt):
    """
    Function for decoding alloc event
    Accepting transaction receipt as parameter
    """
    #Reading abi that have alloc event
    with open(ABI_PATH, 'r') as abi_config:
        abi = json.load(abi_config)
    contract = web3.eth.contract(
        address=CONTRACT_ADDRESS, abi=abi)
    decoded_event = contract.events.alloc().processReceipt(receipt)
    for alloc_event in decoded_event:
        print(
            '--------------Alloc Event---------------------'
            '\nevent: ', alloc_event['event'],
            '\n_address: ', alloc_event['args']['_address'],
            '\n_share: ', alloc_event['args']['_share'],
            '\nlogIndex: ', alloc_event['logIndex'],
            '\ntransactionIndex: ', alloc_event['transactionIndex'],
            '\ntransactionHash: ', alloc_event['transactionHash'].hex(),
            '\naddress: ', alloc_event['address'],
            '\nblockHash: ', alloc_event['blockHash'].hex(),
            '\nblockNumber: ', alloc_event['blockNumber'],
        )

