import json
import asyncio
import warnings
from web3 import Web3
from mint_decoder import decode_mintevent
from burn_decoder import decode_burnevent
from alloc_decoder import decode_allocevent
from config import PROVIDER, CONTRACT_ADDRESS, ABI_PATH

warnings.filterwarnings("ignore")
web3 = Web3(Web3.HTTPProvider(PROVIDER))
with open(ABI_PATH, 'r') as abi_config:
    abi = json.load(abi_config)

contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)


def handle_event(event):
    """
    Function for handle events 
    """
    txn_hash = event['transactionHash'].hex() # Getting Transaction hash
    receipt = web3.eth.getTransactionReceipt(txn_hash) # Getting transaction receipt
    decode_mintevent(receipt)  # Call method for decoding Transaction Receipt mint event Logs 
    decode_burnevent(receipt)  # Call method for decoding Transaction Receipt burn event Logs 
    decode_allocevent(receipt) # Call method for decoding Transaction Receipt alloc event Logs 

async def log_loop(event_filter, poll_interval):
    while True:
        for puchaseEvent in event_filter.get_new_entries():
            handle_event(puchaseEvent)
        await asyncio.sleep(poll_interval)


def main():
    if web3.isConnected():
        print('Connected. Listening for purchase transactions')
    # create a filter for the latest block and look for the puchaseEvent on smart contract
    event_filter = contract.events.puchaseEvent.createFilter(fromBlock='latest')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(event_filter, 2)))
    finally:
        # close loop to free up system resources
        loop.close()


if __name__ == "__main__":
    main()
