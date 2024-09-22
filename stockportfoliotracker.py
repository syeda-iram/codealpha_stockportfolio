pip install requests pandas matplotlib

portfolio = {
    "AAPL": {"shares": 10, "buy_price": 150.0},
    "GOOG": {"shares": 5, "buy_price": 2000.0}
}

import requests

def get_stock_price(symbol):
    api_key = 'KYHWDRIVQ0AGSBDE'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    
    # Extract latest stock price
    price = float(data["Time Series (1min)"][next(iter(data["Time Series (1min)"]))]["4. close"])
    return price

def add_stock(symbol, shares, buy_price):
    portfolio[symbol] = {"shares": shares, "buy_price": buy_price}
    print(f"{symbol} added to portfolio.")
    
def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"{symbol} removed from portfolio.")
    else:
        print(f"{symbol} not found in portfolio.")
        
def calculate_performance(symbol):
    if symbol in portfolio:
        current_price = get_stock_price(symbol)
        shares = portfolio[symbol]["shares"]
        buy_price = portfolio[symbol]["buy_price"]
        current_value = shares * current_price
        purchase_value = shares * buy_price
        profit_loss = current_value - purchase_value
        print(f"Current value: {current_value}, Profit/Loss: {profit_loss}")
    else:
        print(f"{symbol} not found in portfolio.")
        
def view_portfolio():
    for symbol in portfolio:
        current_price = get_stock_price(symbol)
        shares = portfolio[symbol]["shares"]
        buy_price = portfolio[symbol]["buy_price"]
        current_value = shares * current_price
        print(f"{symbol}: {shares} shares | Buy Price: {buy_price} | Current Price: {current_price} | Current Value: {current_value}")

import requests
import matplotlib.pyplot as plt

def plot_stock(symbol):
    # Fetch stock data from an API (e.g., Alpha Vantage)
    api_key = 'KYHWDRIVQ0AGSBDE'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    
    # Extract time and closing price data
    # Check if "Time Series (1min)" exists in the response
    if "Time Series (1min)" not in data:
        print("Error: Time Series data not found in the response. Please check the API key and symbol.")
        return
    
    time_series = data["Time Series (1min)"]
    
    # Sort the times for plotting
    times = sorted(time_series.keys())
    closing_prices = [float(time_series[time]["4. close"]) for time in times]
    
    # Plot the data
    plt.figure(figsize=(30, 5))
    plt.plot(times, closing_prices, label=f'{symbol} Stock Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title(f'{symbol} Stock Price Over Time')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

while(True):
    print(
        "\t\t\t Stock Portfolio Tracker \n"
        "\t\t\t\t Main Menu \n"
        "1. Add Stock \n"
        "2. Remove Stock \n"
        "3. Calculate Stock Performance \n"
        "4. View Portfolio \n"
        "5. Plot Stock Price \n"
        "6. Exit"
        )

    while (True):
        option = int(input("Please select an option: "))
        if option < 1 or option > 6:
            print("Wrong option selected! \n"
                  "Please Try Again... \n")
            continue
        else:
            break

    if option == 1:
        print("\n --- Adding Stock --- \n")
        symbol = input("Enter the Stock's Ticker Symbol: ").upper()
        shares = int(input("Enter the number of shares: "))
        buy_price = float(input("Enter the buying price: "))
        add_stock(symbol, shares, buy_price)
    
    elif option == 2:
        print("\n --- Removing Stock --- \n")
        symbol = input("Enter the Stock's Ticker Symbol: ").upper()
        remove_stock(symbol)
    
    elif option == 3:
        print("\n --- Calculating Stock Performance --- \n")
        symbol = input("Enter the Stock's Ticker Symbol: ").upper()
        calculate_performance(symbol)
    
    elif option == 4:
        print("\n --- Portfolio --- \n")
        view_portfolio()
    
    elif option == 5:
        print("\n --- Stock Price Plotter --- \n")
        symbol = input("Enter Stock Symbol: ").upper().strip()
        print('\n')
        plot_stock(symbol)
        
    elif option == 6:
        print("Exiting the program... \n"
             "\t\t\t Thank You for Visiting!"
             )
        break
    
    print('\n\n')
