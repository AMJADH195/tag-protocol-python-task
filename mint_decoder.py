import json
import warnings
from web3 import Web3
from config import PROVIDER, MINT_CONTRACT_ADDRESS, MINT_ABI_PATH

warnings.filterwarnings("ignore")
web3 = Web3(Web3.HTTPProvider(PROVIDER))


def decode_mintevent(receipt):
    """
    Function for decoding mint event
    Accepting transaction receipt as parameter
    """
    # Reading ABI that have mintEvent
    with open(MINT_ABI_PATH, 'r') as abi_config:
        mint_abi = json.load(abi_config)
    mint_contract = web3.eth.contract(
        address=MINT_CONTRACT_ADDRESS, abi=mint_abi)
    decoded_event = mint_contract.events.mintEvent().processReceipt(receipt)
    for mint_event in decoded_event:
        print(
            "----------------Mint Event------------------",
            "\nevent: ", mint_event['event'],
            "\n_id: ", mint_event['args']['_id'],
            "\n_hash: ", mint_event['args']['_id'],
            "\n_counter: ", mint_event['args']['_counter'],
            "\nlogIndex: ", mint_event['logIndex'],
            "\ntransactionIndex: ", mint_event['transactionIndex'],
            "\ntransactionHash: ", mint_event['transactionHash'].hex(),
            "\naddress: ", mint_event['address'],
            "\nblockHash: ", mint_event['blockHash'].hex(),
            "\nblockNumber: ", mint_event['blockNumber']

        )
