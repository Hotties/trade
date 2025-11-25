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
daily_stats_list = []

## df_krx 순회 하면서 새로운 객체 생성 
# (krx/code/name/)
## krx/code/name/close/date
## krx/code/name/close/5day/20day/60day/120day/volume
df_krx_subset = df_krx[['Code', 'Name']]

stock_info_list = [
    stock_info(
        code = row.Code,
        country = 'KRX',
        name = row.Name
    )
    for row in df_krx_subset.itertuples()
]


print("complete making stock_info_list")

end_date = datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.now()-timedelta(days=120)).strftime('%Y-%m-%d')

all_daily_data_df = pd.DataFrame()

for stock in stock_info_list:
    df = fdr.DataReader( stock.code,start=start_date,end=end_date)
    
    df['Code'] = stock.code

    df_subset = df[['Code', 'Close', 'Volume']]

    all_daily_data_df = pd.concat([all_daily_data_df, df_subset])

all_daily_data_df = all_daily_data_df.reset_index(names=['Date'])
all_daily_data_df['Date_str'] = all_daily_data_df['Date'].dt.strftime('%Y-%m-%d')

print("complete making all_daily_date_df")

daily_price_list = [
    daily_price(
        code = row.Code,
        date = row.Date_str,
        close = row.Close,
        volume = row.Volume
    )
    for row in all_daily_data_df.itertuples()
]
print(daily_stats_list)

# # for i in Codes:
# #     df = fdr.DataReader( i,start=start_date,end=end_date)
# #     df_close = {}
# #     df_close['MA5'] = df['Close'].rolling(window=5).mean()
# #     df_close['MA20'] = df['Close'].rolling(window=20).mean()
# #     df_close['MA60'] = df['Close'].rolling(window=60).mean()
# #     df_close['MA120'] = df['Close'].rolling(window=120).mean()
# #     print(df_close)
