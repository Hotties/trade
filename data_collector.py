import pandas as pd
import FinanceDataReader as fdr
from first_played import is_ran
from datetime import datetime, timedelta
from db.data_class import stock_info, daily_price, daily_stats

# if not is_ran: ## 처음실행 할때

#     df_krx = fdr.StockListing('KRX')
#     df_krx_code = df_krx.Code
#     end_date = datetime.now().strftime('%Y-%m-%d')
#     start_date = (datetime.now()-timedelta(days=120)).strftime('%Y-%m-%d')
#     df = fdr.DataReader( "019175",start=end_date,end=end_date)

df_krx = fdr.StockListing('KRX')
stock_info_list = []
daily_price_list = []
daily_stats_list = []

## df_krx 순회 하면서 새로운 객체 생성 
# (krx/code/name/)
## krx/code/name/close/date
## krx/code/name/close/5day/20day/60day/120day/volume

Codes = df_krx['Code'].tolist()
Names = df_krx['Name'].tolist()
print(Codes)
stock_info_zip = list(zip(Codes,Names))

for i,j in stock_info_zip:
    stock_info_obj = stock_info(i,'KRX',j)
    stock_info_list.append(stock_info_obj)

end_date = datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.now()-timedelta(days=120)).strftime('%Y-%m-%d')
df = fdr.DataReader( '000490',start=end_date,end=end_date)
print(df)
# for i in Codes:
#     print(i)
#     df = fdr.DataReader( i,start=start_date,end=end_date)
#     df = df.reset_index()
#     Date_list = df['Date'].tolist()
#     Close_list = df['Close'].tolist()
#     Volume_list = df['Volume'].tolist()
#     daily_price_zip = list(zip(Date_list,Close_list,Volume_list))
    
#     for j,k,l in daily_price_zip:
#         daily_price_obj = daily_price(i,j,k,l)
#         daily_price_list.append(daily_price_obj)

# for i in Codes:
#     df = fdr.DataReader( i,start=start_date,end=end_date)
#     df_close = {}
#     df_close['MA5'] = df['Close'].rolling(window=5).mean()
#     df_close['MA20'] = df['Close'].rolling(window=20).mean()
#     df_close['MA60'] = df['Close'].rolling(window=60).mean()
#     df_close['MA120'] = df['Close'].rolling(window=120).mean()
#     print(df_close)
