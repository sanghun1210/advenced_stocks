import pandas as pd
from datetime import datetime

def main():

    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = "total_df_" + current_date+ ".csv"
    print(filename)
    df = pd.read_csv(filename, sep='\t', encoding='utf-8')

    print(df.tail())   

    # ROE 기준으로 등수 매기기
    df['ROE_Rank'] = df['ROE'].rank(ascending=False, method='min')

    # PM 기준으로 등수 매기기
    #df['PM_Rank'] = df['PM'].rank(ascending=False, method='min')
    df['EY_Rank'] = df['EY'].rank(ascending=False, method='min')

    # 두 등수의 합산 등수 매기기
    #df['Total_Rank'] = df['ROE_Rank'] + df['PM_Rank']
    df['Total_Rank'] = df['ROE_Rank'] + df['EY_Rank']

    # 합산 등수로 정렬
    df_sorted = df.sort_values('Total_Rank')

    print(df_sorted)
    sorted_filename = "df_sorted" + current_date+ "_ey.csv"
    df_sorted.to_csv(sorted_filename, sep='\t', encoding='utf-8')






if __name__ == "__main__":
    # execute only if run as a script
    main()