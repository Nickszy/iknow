import akshare as ak 
import pandas as pd 
def get_price(code,start_date = "20200101",end_date: str ="20230101",period: str = "daily",adjust: str = ""):
    return ak.stock_zh_a_hist(
        symbol= code,
        start_date=start_date,
        end_date= end_date,
        adjust= adjust
    )

def get_bt_price(code,start_date = "20200101",end_date: str ="20230101",period: str = "daily",adjust: str = ""):
    df = ak.stock_zh_a_hist(
        symbol= code,
        start_date=start_date,
        end_date= end_date,
        adjust= adjust
    )
    df.rename({
        "日期":"Date",
        "开盘":'Open',
        "收盘":"Close",
        "最高":"High",
        "最低":"Low",
        "成交量":"Volume"
        },
            axis=1,
            inplace= True)
    df.index = pd.DatetimeIndex(df.Date)
    df["OpenInterest"] = 1
    return df[["Open","High","Low","Close","Volume","OpenInterest"]]
    
if __name__ == "__main__":
    print(get_bt_price('300033',end_date='20230101'))
