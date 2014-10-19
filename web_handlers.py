import pdb
import logging
import cgi
import os
import json

import webapp2
import jinja2

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

JINJA_ENV = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENV.get_template('templates/index.html')
        self.response.write(template.render(template_values))

class APIHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        d = {}
        for symb in SP100:
            with open(symb, 'rb') as f:
                try:
                    d[symb] = float(pickle.load(f))
                except Exception as e:
                    pass
                    self.response.write(str(e) + '\n')
        body = {'update': False, 'data': self.process(d)}
        self.response.write(json.dumps(body))

    def process(self, d):
        return ', '.join('%s: %.2f' % (symb, float(d.get(symb, 0))) for symb in sorted(d))

    def format(self, s):
        try:
            return '%.2f' % float(s)
        except:
            return 'Unv'

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
    ('/api', APIHandler)
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()
