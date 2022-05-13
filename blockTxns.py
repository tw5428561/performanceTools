from cProfile import label
from pprint import pprint
from web3 import Web3
from web3.auto import w3
import json
from web3.middleware import geth_poa_middleware
import time
import matplotlib.pyplot as plt
import numpy as np


def blockTxns():

    # 链接 rpc
    teleportClient = Web3(Web3.HTTPProvider('https://teleport-localvalidator.qa.davionlabs.com/'))
    teleportClient.middleware_onion.inject(geth_poa_middleware, layer=0)
    last = teleportClient.eth.blockNumber
    data = [[],[]]
    for i in range(last-100, last):
        block = teleportClient.eth.getBlock(i)
        txns = len(block.transactions)
        pprint([block.number,block.timestamp,txns])
        data[0].append(i)
        data[1].append(txns)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ax.plot_date(k[0],k[1],'go--')
    ax.plot(data[0],data[1],'go--')

    ax.set_title('Txns per block')
    ax.set_xlabel('blockNums')
    ax.set_ylabel('Txns', fontdict={"family": "Times New Roman", "size": 25})

    ax.set_xticks(np.arange(data[0][0],data[0][-1]+10,10))
    fig.autofmt_xdate()

    plt.show()


if __name__ == "__main__":
    blockTxns()

