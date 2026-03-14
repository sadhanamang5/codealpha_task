stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140
}

total = 0
for stock in stocks:
    qty = int(input(f"Enter quantity for {stock}: "))
    total += qty * stocks[stock]

print("Total Investment Value:", total)