from pprint import pprint
from web3 import Web3
from web3.middleware import geth_poa_middleware
import matplotlib.pyplot as plt
import argparse
import time

def blockTxns(bs: int, be: int, gap: int = 100):

    # 链接 rpc
    # qa https://teleport-localvalidator.qa.davionlabs.com/
    # testNet https://dataseed.testnet.teleport.network
    teleportClient = Web3(Web3.HTTPProvider('https://dataseed.testnet.teleport.network/'))
    teleportClient.middleware_onion.inject(geth_poa_middleware, layer=0)
    # block-txns 的二维数组
    data = [[],[],[]]
    # 汇总 txns
    count = 0

    if be == 0:
        be = teleportClient.eth.blockNumber
    if bs == 0 or gap != 100:
        bs = be - gap

    for i in range(bs, be):
        block = teleportClient.eth.getBlock(i)
        txns = len(block.transactions)
        count += txns

        pprint([block.number,block.timestamp,txns])

        data[0].append(block.timestamp)
        print(f"append(i): {i}")
        # data[0].append(i)
        data[1].append(txns)

        x = time.localtime(block.timestamp)
        timeStr=time.strftime('%Y-%m-%d %H:%M:%S',x)
        data[2].append(timeStr)

    print(f"上链的txns总数为: {count}")

    fig = plt.figure()
    ax = fig.add_subplot(111)

    print(f"data[0]: {data[0]}")
    print(f"data[1]: {data[1]}")

    ax.plot(data[0],data[1],'go--')

    ax.set_title('Txns per block')
    ax.set_xlabel('time')
    ax.set_ylabel('Txns', fontdict={"family": "Times New Roman", "size": 25})

    ax.set_xticks(data[0],data[2])
    fig.autofmt_xdate()

    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.description='支持定义blockNum,或者获取最新区块'
    parser.add_argument("-bs", "--blockStart", help="起始区块", dest="bs", type=int, default=0)
    parser.add_argument("-be", "--blockEnd", help="截止区块", dest="be", type=int, default=0)
    parser.add_argument("-g", "--gap", help="区块间隔,用于自动获取起始区块", dest="g", type=int, default=100)
    args = parser.parse_args()

    blockTxns(args.bs,args.be,args.g)

