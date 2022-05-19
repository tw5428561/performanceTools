from cProfile import label
from pprint import pprint
from web3 import Web3
from web3.auto import w3
import json
from web3.middleware import geth_poa_middleware
import time
import matplotlib.pyplot as plt
import numpy as np
import argparse
import time

fig = plt.figure()
ax = fig.add_subplot(111)
# ax.plot_date(k[0],k[1],'go--')
ax.plot([1652867941,1652867946,1652867948],[3,4,5],'go--')

ax.set_title('name')
ax.set_xlabel('x_name')
ax.set_ylabel('y_name', fontdict={"family": "Times New Roman", "size": 25})

x = time.localtime(1652867938)
timeStr=time.strftime('%Y-%m-%d %H:%M:%S',x)
print(f"timeStr: {timeStr}")

ax.set_xticks([1652867941,1652867946,1652867948],["2020-08-03 17:40:33","2020-08-03 17:40:33","2020-08-03 17:40:33"])
fig.autofmt_xdate()

plt.show()