from featureExtraction import UsefulFeatures
import argparse
from crawl import Crawl

"""
To test a legitimate/phishing URL, the following URLs below can help. Feel free to use another one is you so please.
to run this demo code, type the following into terminal: python3 demo.py --url "http://www.agencias3voeazul.com"

===Legit URLs====
https://facebook.com
https://qq.com 

===Phihsing URLs====
http://505caipiao.com/
http://beeschage.com/

"""

def get_prediction(args):
    if args.predict:
        value = {0: 'This is a phishing website', 1: 'This is a legit website'}
        print('The URL queried is: {}'.format(args.url), '\n')
        url = args.url
        features = UsefulFeatures(url)
        print(value[features.predict(args)])

def crawl(args):
    if args.crawl:
        crawler = Crawl(args) 
        crawler.crawl()
    

if '__main__' == __name__:
    parser = argparse.ArgumentParser(description='URL Prediction')
    parser.add_argument('--url', nargs='?', type=str, default='https://yahoo.com', help='the url to predict')
    parser.add_argument('--num_neighbors', nargs='?', type=int, default=3,
                            help='max number of links to crawl in a new url')
    parser.add_argument('--crawl_depth', nargs='?', type=int, default=3,
                            help='the depth of crawling a url')
    parser.add_argument('--resume', nargs='?', type=str, default=None,
                            help='the url index to resume crawling')
    parser.add_argument('--batch_size', nargs='?', type=int, default=15,
                            help='Batch Size')
    parser.add_argument('--database_name', nargs='?', type=str, default='fullstack',
                            help='the name of the Mongo database we will use')
    parser.add_argument('--url_table_name', nargs='?', type=str, default='alexa_demo',
                            help='the name of the ip_table')
    parser.add_argument('--data_loc', nargs='?', type=str, default='../data/alexa.csv',
                            help='data location')
    parser.add_argument('--features_table_name', nargs='?', type=str, default='feature_table',
                            help='the name of the feature_table')
    parser.add_argument('--num_urls', nargs='?', type=int, default=10000,
                            help='total number of urls o list to crawl')
    parser.add_argument('--http_timeout', nargs='?', type=int, default=5,
                            help='timeout for http requests')
    parser.add_argument('--socket_timeout', nargs='?', type=int, default=3,
                            help='timeout for so')
    parser.add_argument('--http_retries', nargs='?', type=int, default=1,
                            help='number of retry counts')
    parser.add_argument('--start', nargs='?', type=int, default=1,
                            help='url index to start from')
    parser.add_argument('--predict', nargs='?', type=bool, default=False, help='make a prediction')
    parser.add_argument('--crawl', nargs='?', type=bool, default=False, help='crawl websites')
    args = parser.parse_args()
    get_prediction(args)
    crawl(args)
