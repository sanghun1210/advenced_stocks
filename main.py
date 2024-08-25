import pandas as pd
import FinanceDataReader as fdr
import fundametal_analysis
from datetime import datetime, timedelta
from data_handler import StockDataHandler
import csv

def get_tickers():
    #df_krx = stock.get_market_ticker_list('240818',market='ALL')
    df_krx = fdr.StockListing('KRX')
    with open('tickers.csv','w') as file :
        write = csv.writer(file)
        write.writerow(df_krx)
    return df_krx


# 행 추가 함수 정의
def add_row(df, code, name, roe, pm):
    new_row = pd.DataFrame({'Code': code, 'Name': name, 'ROE': roe, 'PM': pm}, index=[0])
    comb = pd.concat([df, new_row])
    return comb

#ROE : 자본이익률
#PM : 이익수익률

def get_period():
    current_date = datetime.now()
    result_date = current_date - timedelta(days=500)

    end_date = current_date.strftime('%Y-%m-%d')
    start_date = result_date.strftime('%Y-%m-%d')
    return start_date, end_date

def get_magic_symbols(code, close_price):
    fa = fundametal_analysis.FundamentalAnalysis(code)
    roe, eps = fa.get_base_financial_data()
    pm = (eps / close_price) * 100
    ey = fa.get_earnings_yield(close_price)
    return roe, pm, ey

def main():
    # 빈 DataFrame 생성
    print(pd.__version__)
    df_krx = get_tickers()
    start, end = get_period()
    total_df = pd.DataFrame(columns=['Code', 'Name', 'ROE', 'PM'])
    print(len(df_krx))
    for code, name in zip(df_krx['Code'], df_krx['Name']) :
        try:
            print(code)
            data_handler = StockDataHandler(code, start, end)
            if data_handler.check_valid_data() == False:
                continue 
            daily_df = data_handler.get_daily_data()
            roe, pm, ey = get_magic_symbols(code, daily_df['trade_price'].iloc[-1])
            total_df = add_row(total_df, code, name, roe, ey)
        except Exception as e:    
            print("raise error ", e)

    total_df.to_csv("total_df_20240825.csv", sep='\t', encoding='utf-8')

if __name__ == "__main__":
    # execute only if run as a script
    main()
