from lxml import html
import requests
from time import sleep
import json
import argparse
from collections import OrderedDict
from time import sleep


def parse():
    url = "https://finance.yahoo.com/quote/%5EDJI/"
    response = requests.get(url, verify=False)
    # print("Parsing %s" % (url))
    # sleep(2)
    parser = html.fromstring(response.text)
    # print(response.text)
    # summary_table = parser.xpath('//div[contains(@data-test,"summary-table")]//tr')
    # summary_table = parser.xpath('//div[contains(@class,"summary-table")]//tr')
    # summary_table = parser.xpath('//span[contains(@class,"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"]')
    summary_table = parser.xpath('// *[ @ id = "quote-header-info"] / div[3] / div / span')
    # print(summary_table[0].text)
    print(summary_table[0].text)
    # // *[ @ id = "quote-header-info"] / div[3] / div / div / span[1]
    # // *[ @ id = "quote-header-info"] / div[3] / div / div

    # summary_data = OrderedDict()
    # dowRequest = "https://finance.yahoo.com/quote/%5EDJI/"
    # summary_json_response = requests.get(dowRequest)
    # print(summary_json_response.text)
    # .xpath('.//td[contains(@class,"C(black)")]//text()')
    try:
        print("break")
        # print(str(summary_table))
        # json_loaded_summary = json.loads(summary_json_response.text)
        # print(json_loaded_summary)
        # dow = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["targetMeanPrice"]['raw']
        # print(json_loaded_summary)
        # y_Target_Est = json_loaded_summary["quoteSummary"]["result"][0]["financialData"]["targetMeanPrice"]['raw']
        # earnings_list = json_loaded_summary["quoteSummary"]["result"][0]["calendarEvents"]['earnings']
        # eps = json_loaded_summary["quoteSummary"]["result"][0]["defaultKeyStatistics"]["trailingEps"]['raw']
        # datelist = []
        # for i in earnings_list['earningsDate']:
        #     datelist.append(i['fmt'])
        # # print(summary_table)
        # earnings_date = ' to '.join(datelist)
        # # print(summary_table)
        # for table_data in summary_table:

        #     raw_table_key = table_data.xpath('.//td[contains(@class,"C(black)")]//text()')
        #     raw_table_value = table_data.xpath('.//td[contains(@class,"Ta(end)")]//text()')
        #     # print(raw_table_key)
        #     table_key = ''.join(raw_table_key).strip()
        #     table_value = ''.join(raw_table_value).strip()
        #     summary_data.update({table_key: table_value})
        # summary_data.update(
        #     {'1y Target Est': y_Target_Est, 'EPS (TTM)': eps, 'Earnings Date': earnings_date, 'ticker': ticker,
        #      'url': url})
        # return response.text
        # return summary_data
        # print("break")
        # print(summary_data)
    except:
        print("Failed to parse json response")
        return {"error": "Failed to parse json response"}


if __name__ == "__main__":
    # argparser = argparse.ArgumentParser()
    # argparser.add_argument('ticker', help='')
    # args = argparser.parse_args()
    # ticker = args.ticker
    # print("Fetching data for %s" % (ticker))
    scraped_data = parse()
    # print("Writing data to output file")
    # with open('%s-ssummary.json' % (ticker), 'w') as fp:
    #     json.dump(scraped_data, fp, indent=4)