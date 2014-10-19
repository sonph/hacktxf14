#!/usr/bin/env python

import blpapi
import pickle

SP100 = ['AAPL', 'ABBV', 'ABT', 'ACN', 'AIG', 'ALL', 'AMGN', 'AMZN', 'APA',
'APC', 'AXP', 'BA', 'BAC', 'BAX', 'BIIB', 'BK', 'BMY', 'BRK.B', 'C', 'CAT',
'CL', 'CMCSA', 'COF', 'COP', 'COST', 'CSCO', 'CVS', 'CVX', 'DD', 'DIS', 'DOW',
'DVN', 'EBAY', 'EMC', 'EMR', 'EXC', 'F', 'FB', 'FCX', 'FDX', 'FOXA', 'GD', 'GE',
'GILD', 'GM', 'GOOG', 'GS', 'HAL', 'HD', 'HON', 'HPQ', 'IBM', 'INTC', 'JNJ',
'JPM', 'KO', 'LLY', 'LMT', 'LOW', 'MA', 'MCD', 'MDLZ', 'MDT', 'MET', 'MMM',
'MO', 'MON', 'MRK', 'MS', 'MSFT', 'NKE', 'NOV', 'NSC', 'ORCL', 'OXY', 'PEP',
'PFE', 'PG', 'PM', 'QCOM', 'RTN', 'SBUX', 'SLB', 'SO', 'SPG', 'T', 'TGT', 'TWX',
'TXN', 'UNH', 'UNP', 'UPS', 'USB', 'UTX', 'V', 'VZ', 'WAG', 'WFC', 'WMT', 'XOM']

SERVER = '10.8.8.1'
PORT = 8194

def main():
    opts = blpapi.SessionOptions()
    opts.setServerHost(SERVER)
    opts.setServerPort(PORT)
    ses = blpapi.Session(opts)
    ses.start()
    ses.openService('//blp/mktdata')
    sub = blpapi.SubscriptionList()

    for i, symb in enumerate(SP100):
        sub.add(symb + ' US Equity', 'LAST_PRICE,BID,ASK', '', blpapi.CorrelationId(i))

    ses.subscribe(sub)

    while True:
        event = ses.nextEvent()
        for msg in event:
            process(msg)

def process(msg):
    value = 'Unv'
    try:
        name = SP100[msg.correlationIds()[0].value()]
        try:
            value = msg.getValueAsString('LAST_PRICE')
            with open(name, 'wb') as f:
                pickle.dump(value, f)
        except:
            value = 'Unv'
    except:
        pass

if __name__ == '__main__':
    main()
