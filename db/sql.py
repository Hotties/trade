# sql.py

## CREATE 

CREATE_STOCK_INFO = """
    CREATE TABLE IF NOT EXISTS STOCK_INFO(
        code INT PRIMARY KEY,
        country CHAR(50),
        name CHAR(50)
    )
"""

CREATE_DAILY_PRICE = """
        CREATE TABLE IF NOT EXISTS DAILY_PRICE(
        code INT PRIMARY KEY,
        date DATE PRIMARY KEY,
        close INT,
        volume INT,
        PRIMARY KEY (code, date),
        FOREIGN KEY code REFERENCES STOCK_INFO(code)
    )
"""
CREATE_DAILY_STATS = """
    CREATE TABLE IF NOT EXISTS DAILY_STATS(
        code INT,
        date DATE,
        ma_5day INT,
        ma_20day INT,
        ma_60day INT,
        ma_120day INT,
        PRIMARY KEY (code, date), -- code와 date를 묶어 복합 기본 키 설정
        
        -- code는 STOCK_INFO를 참조
        FOREIGN KEY (code) REFERENCES STOCK_INFO(code), 
        
        -- (code, date) 쌍은 DAILY_PRICE 테이블의 (code, date) 쌍을 참조
        FOREIGN KEY (code, date) REFERENCES DAILY_PRICE(code, date) 
    )
"""
