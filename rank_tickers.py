import pandas as pd

def main():
    df = pd.read_csv('total_df_20240825.csv', sep='\t', encoding='utf-8')

    print(df.tail())   

    # ROE 기준으로 등수 매기기
    df['ROE_Rank'] = df['ROE'].rank(ascending=False, method='min')

    # PM 기준으로 등수 매기기
    df['PM_Rank'] = df['PM'].rank(ascending=False, method='min')

    # 두 등수의 합산 등수 매기기
    df['Total_Rank'] = df['ROE_Rank'] + df['PM_Rank']

    # 합산 등수로 정렬
    df_sorted = df.sort_values('Total_Rank')

    print(df_sorted)
    df_sorted.to_csv("df_sorted_20240825.csv", sep='\t', encoding='utf-8')






if __name__ == "__main__":
    # execute only if run as a script
    main()