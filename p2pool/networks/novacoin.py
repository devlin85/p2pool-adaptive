from p2pool.bitcoin import networks

PARENT=networks.nets['novacoin']
SHARE_PERIOD=15 # seconds
CHAIN_LENGTH=12*60*60//10 # shares
REAL_CHAIN_LENGTH=12*60*60//10 # shares
TARGET_LOOKBEHIND=200 # shares
SPREAD=3 # blocks
IDENTIFIER='e037d5b8c6923610'.decode('hex')
PREFIX='7208c1a53ef659b0'.decode('hex')
P2P_PORT=29946
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=True
WORKER_PORT=8890
BOOTSTRAP_ADDRS='p2pool.e-pool.net 37.57.95.59:8777 81.200.241.54:8777 82.200.205.39:8777 82.234.193.23:8777 85.198.114.251:8777 85.234.62.99:8777 89.239.190.22:8777 89.250.210.94:8777 94.198.0.39:8777 95.84.138.99:8777 109.238.244.73:8777 176.37.148.85:8777 178.19.249.43:8777 178.159.127.151:8777 188.130.184.1:8777 212.98.191.90:8777 212.113.35.38:8777'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-alt'
VERSION_CHECK=lambda v: v >= 60016
