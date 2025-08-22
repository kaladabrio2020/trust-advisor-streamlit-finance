import yfinance


def verify_symbol(symbol: str) -> bool:
    dados = yfinance.download(symbol, period="1d")
    return not dados.empty

def exist_stocks_crypto_index(symbol: str) -> bool:
    return symbol in ["^BVSP", "^GSPC", "^DJI", "^IXIC", "^GDAXI", "^FCHI", "^N225"]