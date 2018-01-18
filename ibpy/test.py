# Reference Doc is:
# https://github.com/blampe/IbPy/wiki/Getting-Started

from ib.opt import ibConnection, message

def my_account_handler(msg):
    # ... do something with account msg ...
    print('account msg', msg)

def my_tick_handler(msg):
    # ... do something with market data msg ...
    print('market msg', msg)

connection = ibConnection()
connection.register(my_account_handler, 'UpdateAccountValue')
connection.register(my_tick_handler, 'TickSize', 'TickPrice')
connection.connect()
# connection.reqAccountUpdates(...)