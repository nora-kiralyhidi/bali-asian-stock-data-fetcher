import pandas as pd
import yfinance as yf
from bali_memory import init_database, save_report

# Bali - Asian stock market data fetcher
# Target markets: Hongkong, China and American-listed Chinese companies

portfolio = [
    # --- Hongkong Stock Exchange ---
    {"Sektor": "Tech / AI", "Vállalat": "Tencent", "Ticker": "0700.HK"},
    {"Sektor": "Tech / AI", "Vállalat": "Alibaba", "Ticker": "9988.HK"},
    {"Sektor": "Tech / AI", "Vállalat": "Xiaomi", "Ticker": "1810.HK"},
    {"Sektor": "Tech / AI", "Vállalat": "Baidu", "Ticker": "9888.HK"},
    {"Sektor": "Tech / AI", "Vállalat": "Meituan", "Ticker": "3690.HK"},
    {"Sektor": "Tech / AI", "Vállalat": "NetEase", "Ticker": "9999.HK"},
    {"Sektor": "Tech / AI", "Vállalat": "Kuaishou", "Ticker": "1024.HK"},
    {"Sektor": "Félvezetők", "Vállalat": "SMIC", "Ticker": "0981.HK"},
    {"Sektor": "Autóipar", "Vállalat": "BYD", "Ticker": "1211.HK"},
    {"Sektor": "Autóipar", "Vállalat": "NIO", "Ticker": "9866.HK"},
    {"Sektor": "Autóipar", "Vállalat": "Li Auto", "Ticker": "2015.HK"},
    {"Sektor": "Telekom", "Vállalat": "China Mobile", "Ticker": "0941.HK"},
    {"Sektor": "Energia", "Vállalat": "CNOOC", "Ticker": "0883.HK"},
    {"Sektor": "Pénzügy", "Vállalat": "China Construction Bank", "Ticker": "0939.HK"},
    {"Sektor": "Pénzügy", "Vállalat": "ICBC", "Ticker": "1398.HK"},
    {"Sektor": "Pénzügy", "Vállalat": "Ping An Insurance", "Ticker": "2318.HK"},
     
    # --- Shanghai Stock Exchange ---
    {"Sektor": "Fogyasztási cikkek", "Vállalat": "Kweichow Moutai", "Ticker": "600519.SS"},
    {"Sektor": "Pénzügy", "Vállalat": "Ping An Insurance", "Ticker": "601318.SS"},
    {"Sektor": "Pénzügy", "Vállalat": "China Merchants Bank", "Ticker": "600036.SS"},
    {"Sektor": "Bányászat", "Vállalat": "Zijin Mining", "Ticker": "601899.SS"},
    {"Sektor": "Félvezetők", "Vállalat": "SMIC", "Ticker": "688981.SS"},
    {"Sektor": "Energia", "Vállalat": "China Yangtze Power", "Ticker": "600900.SS"},
    {"Sektor": "Megújuló energia", "Vállalat": "LONGi Green Energy", "Ticker": "601012.SS"},
    {"Sektor": "Pénzügy", "Vállalat": "Industrial Bank", "Ticker": "601166.SS"},
    {"Sektor": "Egészségügy", "Vállalat": "Hengrui Medicine", "Ticker": "600276.SS"},

    # --- Shenzhen Stock Exchange ---
    {"Sektor": "Autóipar", "Vállalat": "CATL", "Ticker": "300750.SZ"},
    {"Sektor": "Autóipar", "Vállalat": "BYD", "Ticker": "002594.SZ"},
    {"Sektor": "Technológia", "Vállalat": "Midea Group", "Ticker": "000333.SZ"},
    {"Sektor": "Pénzügy / Fintech", "Vállalat": "East Money", "Ticker": "300059.SZ"},
    {"Sektor": "Technológia", "Vállalat": "Hikvision", "Ticker": "002415.SZ"},
    {"Sektor": "Megújuló energia", "Vállalat": "Sungrow", "Ticker": "300274.SZ"},
    {"Sektor": "Fogyasztási cikkek", "Vállalat": "Wuliangye", "Ticker": "000858.SZ"},
    {"Sektor": "Pénzügy", "Vállalat": "Ping An Bank", "Ticker": "000001.SZ"},
    {"Sektor": "Tech / AI", "Vállalat": "iFlytek", "Ticker": "002230.SZ"},

    # --- Chinese companies listed on American exchanges ---
    {"Sektor": "Tech / AI", "Vállalat": "Alibaba", "Ticker": "BABA"},
    {"Sektor": "Tech / AI", "Vállalat": "Baidu", "Ticker": "BIDU"},
    {"Sektor": "E-kereskedelem", "Vállalat": "JD.com", "Ticker": "JD"},
    {"Sektor": "E-kereskedelem", "Vállalat": "PDD Holdings", "Ticker": "PDD"},
    {"Sektor": "Autóipar", "Vállalat": "NIO", "Ticker": "NIO"},
    {"Sektor": "Autóipar", "Vállalat": "XPeng", "Ticker": "XPEV"},
    {"Sektor": "Autóipar", "Vállalat": "Li Auto", "Ticker": "LI"},
    {"Sektor": "Digitális média", "Vállalat": "Bilibili", "Ticker": "BILI"},
    {"Sektor": "Utazás", "Vállalat": "Trip.com", "Ticker": "TCOM"},
    {"Sektor": "Logisztika", "Vállalat": "ZTO Express", "Ticker": "ZTO"},
    {"Sektor": "Fintech", "Vállalat": "Futu Holdings", "Ticker": "FUTU"},
    {"Sektor": "Ingatlan", "Vállalat": "KE Holdings", "Ticker": "BEKE"},
]
riport_data = []
hibas_tickerek = []
init_database()  # Initialize the database and create the table if it doesn't exist
print("--- Bali (Data Fetcher) is starting the sector-specific data collection ---")
for item in portfolio:
    name = item["Vállalat"]
    ticker = item["Ticker"]
    sektor = item["Sektor"]

    try:
        # Download data for the last 5 days
        print(f"Bali is now downloading data for: {ticker} - {name}")
        data = yf.download(ticker, period="5d", progress=False)
        print(f"Ticker: {ticker} | Empty data: {data.empty}")
        print(data.tail(2))
    
        if not data.empty:
            # Make sure we treat the 'Close' column correctly, whether it's a DataFrame or Series
            close_data = data['Close']
            if isinstance(close_data, pd.DataFrame):
                close_data = close_data.iloc[:, 0]

            First_close = float(close_data.iloc[0])
            Last_close = float(close_data.iloc[-1])

            Change = ((Last_close - First_close) / First_close) * 100
            print(name, First_close, Last_close, Change)

            riport_data.append({
                "Sektor": sektor,
                "Vállalat": name,
                "Ticker": ticker,
                "Aktuális ár (helyi deviza)": round(Last_close, 2),
                "Change az 5 nap alatt (%)": round(Change, 2)
            })
            save_report(sektor, name, ticker, round(Last_close, 2), round(Change, 2))
        else:
            print(f"WARNING: No data available for {name} ({ticker})")
            hibas_tickerek.append(ticker)
    except Exception as e:
        print(f"Error occurred while fetching data for {name} ({ticker}): {e}")
        hibas_tickerek.append(ticker)
# Create the pandas DataFrame from the collected report data, sort it by sector, and reset the index
riport_df = pd.DataFrame(riport_data)
riport_df = riport_df.sort_values(by="Sektor").reset_index(drop=True)
print("Successfully processed stocks:", len(riport_df))

print("Report data:", riport_data)
print("Columns:", riport_df.columns.tolist())
print("Number of data rows:", len(riport_df))

print("\n" + riport_df.to_string(index=False))
print("Failed tickers:", hibas_tickerek)
print("\n--- Bali successfully completed with sector-specific data! ---")
