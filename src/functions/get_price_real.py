import yfinance


def get_price_real(symbol: str, buy_price: float) -> float:
    dados = yfinance.download(symbol, period="1d")
    dados =dados["Close"][0]

    return buy_price/dados