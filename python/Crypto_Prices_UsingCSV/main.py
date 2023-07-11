from pycoingecko import CoinGeckoAPI
import pandas
from datetime import datetime

pd = pandas
df = pd.read_csv("coins.csv")
cg = CoinGeckoAPI()

coin_list = []

# adds date and time to first entry in the list
now = datetime.now()
dt_date = now.strftime("%m/%d/%Y")
dt_time = now.strftime("%H:%M:%S")
date = {'coin': dt_time,
        'price': dt_date}
coin_list.append(date)

# convert dataframe to a dict
coins = {row.i: row.coin for (index, row) in df.iterrows()}

# request coin prices from coingecko
for i, coin in coins.items():
    prices = {}
    price = ""
    coin_val = cg.get_price(ids=coin.lower(), vs_currencies='usd')
    try:
        price = coin_val[coin]['usd']
    except KeyError:
        price = 'NA'
        print(f'Unable to find {coin} price. Could be a spelling error or incorrect id.')
    finally:
        prices["coin"] = coin
        prices["price"] = price
        coin_list.append(prices)
        print(coin)

price_df = pd.DataFrame(coin_list)
price_df.to_csv('crypto_prices.csv', mode="w", index=False)
