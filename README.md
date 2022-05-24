# Listen Purchase transactions on 0xA0961c56A7695336a4aD651639d094Be4EEFC1dd
 
Tested python version 3.10.4 ,
Operating System Ubuntu 20

- To install required packages run ```pip install -r requirements.txt```
- To listen purchase transactions run ```python purchase_listener.py```
- For testing decoding of events run ```python log_tester.py``` it uses a purchase transaction hash occured on the given smart contract
- Sample output of decoded logs of the purchase transaction is saved on output folder
