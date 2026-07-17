import yfinance as yf

nvda = yf.download("NVDA", period="1mo")

print(nvda.head())