import yfinance as yf

class DadosAtivoYahoo:
    def get_price(self, symbol):
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")
        last_price = data['Close'].iloc[-1]
        return last_price

if __name__ == "__main__":
    data = DadosAtivoYahoo()
    print(data.get_price("VALE3.SA"))