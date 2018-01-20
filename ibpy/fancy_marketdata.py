#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ib.ext.Contract import Contract
from ib.opt import ibConnection, message
from time import sleep

# print all messages from TWS
def watcher(msg):
    print msg

# show Bid and Ask quotes
def my_BidAsk(msg):
    if msg.field == 1:
        print ('%s:%s: bid: %s' % (contractTuple[0],
                       contractTuple[6], msg.price))
    elif msg.field == 2:
        print ('%s:%s: ask: %s' % (contractTuple[0], contractTuple[6], msg.price))

def makeStkContract(contractTuple):
    newContract = Contract()
    newContract.m_symbol = contractTuple[0]
    newContract.m_secType = contractTuple[1]
    newContract.m_exchange = contractTuple[2]
    newContract.m_currency = contractTuple[3]
    newContract.m_expiry = contractTuple[4]
    newContract.m_strike = contractTuple[5]
    newContract.m_right = contractTuple[6]
    print ('Contract Values:%s,%s,%s,%s,%s,%s,%s:' % contractTuple)
    return newContract

def create_contract(symbol, sec_type, exch, prim_exch, curr):
    """Create a Contract object defining what will
    be purchased, at which exchange and in which currency.

    symbol - The ticker symbol for the contract
    sec_type - The security type for the contract ('STK' is 'stock')
    exch - The exchange to carry out the contract on
    prim_exch - The primary exchange to carry out the contract on
    curr - The currency in which to purchase the contract"""
    contract = Contract()
    contract.m_symbol = symbol
    contract.m_secType = sec_type
    contract.m_exchange = exch
    contract.m_primaryExch = prim_exch
    contract.m_currency = curr
    return contract


if __name__ == '__main__':
    con = ibConnection(port=7497, clientId=103)
    con.registerAll(watcher)
    showBidAskOnly = True  # set False to see the raw messages
    if showBidAskOnly:
        con.unregister(watcher, message.tickSize, message.tickPrice,
                       message.tickString, message.tickOptionComputation)
        con.register(my_BidAsk, message.tickPrice)
    con.connect()
    sleep(1)
    tickId = 1002

    # Note: Option quotes will give an error if they aren't shown in TWS
    # contractTuple = ('QQQQ', 'STK', 'SMART', 'USD', '', 0.0, '')
    # contractTuple = ('QQQQ', 'OPT', 'SMART', 'USD', '20070921', 47.0, 'CALL')
    #contractTuple = ('ES', 'FUT', 'GLOBEX', 'USD', '200709', 0.0, '')
    # contractTuple = ('ES', 'FOP', 'GLOBEX', 'USD', '20070920', 1460.0, 'CALL')
    contractTuple = ('EUR', 'CASH', 'IDEALPRO', 'USD', '', 0.0, '')

    # contractTuple = ('FB', 'CASH', 'SMART', 'USD', '', 0.0, '')

    stkContract = makeStkContract(contractTuple)

    # goog_contract = create_contract('MSFT', 'STK', 'SMART', 'SMART', 'USD')
    print ('* * * * REQUESTING MARKET DATA * * * *')
    con.reqMktData(tickId, stkContract, '', False)
    sleep(15)
    print ('* * * * CANCELING MARKET DATA * * * *')
    con.cancelMktData(tickId)
    sleep(1)
    con.disconnect()
    sleep(1)
