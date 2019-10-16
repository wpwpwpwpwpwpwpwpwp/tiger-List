######涨停板统计股票池
from jqdatasdk import *
auth('18582326396', 'cdbjwp1995wpwp')
def StockPoolWithPricePool(day,num):
    #yesterday = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")####获取前一天的日期
    data = get_billboard_list(stock_list=None, end_date=day, count=num)####获取最近一年的龙虎榜数据
    data = data.drop_duplicates(['code', 'day'])
    return data
if __name__=='__main__':
   data = StockPoolWithPricePool('2019-10-15')
   print(data)