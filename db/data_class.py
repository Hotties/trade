

class stock_info:
    def __init__(self, code, country, name):
        self.code = code
        self.country = country
        self.name = name
        pass

class daily_price:
    def __init__(self, code, date, close, volume):
        self.code = code
        self.date = date
        self.close = close
        self.volume = volume
        pass

class daily_stats:
    def __init__(self, code, date, ma_5day, ma_20day, ma_60day, ma_120day):
        self.code = code
        self.date = date
        self.ma_5day = ma_5day
        self.ma_20day = ma_20day
        self.ma_60day = ma_60day
        self.ma_120day = ma_120day
        pass