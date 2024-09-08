import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/data.csv')

data['datetime'] = pd.to_datetime(data['datetime'], errors='coerce')

data = data.sort_values(by='datetime')

data['SMA20'] = data['close'].rolling(window=20).mean()
data['SMA50'] = data['close'].rolling(window=50).mean()

plt.figure(figsize=(10,6))
plt.plot(data['datetime'], data['close'], label='Close Price')
plt.plot(data['datetime'], data['SMA20'], label='SMA 20')
plt.plot(data['datetime'], data['SMA50'], label='SMA 50')
plt.title('Simple Moving Average Crossover')
plt.legend()
plt.show()

data['Signal'] = 0
data['Signal'] = data.apply(lambda row: 1 if row['SMA20'] > row['SMA50'] else 0, axis=1)
data['Position'] = data['Signal'].diff()

buy_signals = data[data['Position'] == 1]
sell_signals = data[data['Position'] == -1]

print("Buy signals:")
print(buy_signals[['datetime', 'close']])

print("Sell signals:")
print(sell_signals[['datetime', 'close']])
