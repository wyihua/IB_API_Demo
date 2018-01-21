# ib_api_demo.py
from ib.ext.Contract import Contract
from ib.ext.Order import Order
from ib.opt import Connection, message

import pandas as pd
from .IBWrapper import IBWrapper, contract
from time import sleep

# from ib.ext.AnyWrapper import AnyWrapper
# from ib.ext.EWrapper import EWrapper


# g_getData = 0

def error_handler(msg):
    """Handles the capturing of error messages"""
    print("Server Error: %s" % msg)

def reply_handler(msg):
    """Handles of server replies"""
    tick_type = {0 : "BID SIZE",
             1 : "BID PRICE",
             2 : "ASK PRICE",
             3 : "ASK SIZE",
             4 : "LAST PRICE",
             5 : "LAST SIZE",
             6 : "HIGH",
             7 : "LOW",
             8 : "VOLUME",
             9 : "CLOSE PRICE",
             10 : "BID OPTION COMPUTATION",
             11 : "ASK OPTION COMPUTATION",
             12 : "LAST OPTION COMPUTATION",
             13 : "MODEL OPTION COMPUTATION",
             14 : "OPEN_TICK",
             15 : "LOW 13 WEEK",
             16 : "HIGH 13 WEEK",
             17 : "LOW 26 WEEK",
             18 : "HIGH 26 WEEK",
             19 : "LOW 52 WEEK",
             20 : "HIGH 52 WEEK",
             21 : "AVG VOLUME",
             22 : "OPEN INTEREST",
             23 : "OPTION HISTORICAL VOL",
             24 : "OPTION IMPLIED VOL",
             27 : "OPTION CALL OPEN INTEREST",
             28 : "OPTION PUT OPEN INTEREST",
             29 : "OPTION CALL VOLUME"}

    # tick_data = pd.DataFrame(msg.size, columns = ['tickerId', 'field', 'price', 'canAutoExecute'])
    
    # tick_data["Type"] = tick_data["field"].map(tick_type)
    # msg['Type'] = msg['field'].map(tick_type)
    msgType = 'Undefined'
    if hasattr(msg, 'field'):
        msgType = tick_type[msg.field]

    # msg.type = tick_type[msg.field]
    print("Server Response: %s, %s, msgType = %s" % (msg.typeName, msg, msgType))


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

def create_order(order_type, quantity, action):
    """Create an Order object (Market/Limit) to go long/short.

    order_type - 'MKT', 'LMT' for Market or Limit orders
    quantity - Integral number of assets to order
    action - 'BUY' or 'SELL'"""
    order = Order()
    order.m_orderType = order_type
    order.m_totalQuantity = quantity
    order.m_action = action
    return order

def my_tick_handler(msg):
    print('tick handler', msg)
    

def getMktData():

    # market data connection)
    tws_conn = Connection.create(port=7497, clientId=110) # now there is a problem: I have to change clientId every time to avoid usfarm issue
    tws_conn.connect()

    # Assign the handling function defined above
    tws_conn.register(error_handler, 'Error')
    tws_conn.registerAll(reply_handler)

    create = contract()
    contract_info = create.create_contract('EUR', 'CASH', 'IDEALPRO', 'USD')
    tickedId = 1002
    sleep(10)
    tws_conn.reqMktData(tickedId, contract_info, "", False)
    sleep(10)
    tws_conn.disconnect()





def buyTicket():
    tws_conn = Connection.create(port=7497, clientId=110) # now there is a problem: I have to change clientId every time to avoid usfarm issue
    tws_conn.connect()

    # Assign the handling function defined above
    tws_conn.register(error_handler, 'Error')
    tws_conn.registerAll(reply_handler)

    order_id = 1
    goog_contract = create_contract('FB', 'STK', 'SMART', 'SMART', 'USD')
    # goog_contract = create_contract('EUR', 'STK', 'SMART', 'SMART', 'USD')
    goog_order = create_order('MKT', 50, 'BUY')

    # Use the connection to the send the order to IB
    tws_conn.placeOrder(order_id, goog_contract, goog_order)


    # tws_conn.reqMktData(1002, goog_contract, "", False)



    ##############################
    # Here is the code for retrieveing data from market
    # callback = IBWrapper()
    # callback.initiate_variables()
    create = contract()
    contract_info = create.create_contract('EUR', 'CASH', 'IDEALPRO', 'USD')
    tickedId = 1002
    # tws_conn.reqMarketDataType( MarketDataTypeEnum.DELAYED )

    # tws_conn.placeOrder(1002, contract_info, goog_order)

    sleep(10)
    tws_conn.reqMktData(tickedId, contract_info, "", False)
    sleep(10)

    # tick_data = pd.DataFrame(callback.tick_Price, columns = ['tickerId', 'field', 'price', 'canAutoExecute'])
    
    # tick_data["Type"] = tick_data["field"].map(tick_type)

    # print tick_data
    

    ##############################


    # Disconnect from TWS
    tws_conn.disconnect()