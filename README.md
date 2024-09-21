### Stock Portfolio Tracker

This is a Python-based Stock Portfolio Tracker that allows users to manage and track the performance of their stock investments. The tool integrates with the Alpha Vantage API to fetch real-time stock price data, providing functionalities to add, remove, calculate performance, and visualize stock prices within the portfolio.

### Features
1. **Add Stock**: Users can add stocks to their portfolio by providing the stock's ticker symbol, number of shares, and the buying price.
   
2. **Remove Stock**: Users can remove a stock from their portfolio by entering its ticker symbol.

3. **Calculate Stock Performance**: For a selected stock, the tool calculates the current value of the user's holdings and the profit/loss by comparing the buying price to the current market price.

4. **View Portfolio**: Displays the current portfolio, showing stock symbol, number of shares, buying price, current price, and the current value of each stock.

5. **Plot Stock Price**: Fetches and plots the real-time stock prices for a specific stock, showing its trend over time.

6. **Exit**: Exits the application.

### Libraries Used
- **requests**: For making API calls to Alpha Vantage and retrieving stock data.
- **pandas**: (installed but not used in this current version) For potential future enhancements like storing and analyzing stock data.
- **matplotlib**: Used to plot stock prices over time.

### How It Works

1. **Fetching Stock Price**: 
   The `get_stock_price(symbol)` function fetches the latest stock price for a given stock symbol using the Alpha Vantage API. The stock prices are retrieved at 1-minute intervals, and the latest price is extracted from the response.

2. **Adding Stocks**: 
   The `add_stock(symbol, shares, buy_price)` function allows users to add a stock to the portfolio by providing the symbol, number of shares, and the buying price.

3. **Removing Stocks**: 
   The `remove_stock(symbol)` function enables users to remove a stock from the portfolio by entering the ticker symbol.

4. **Calculating Performance**: 
   The `calculate_performance(symbol)` function calculates the performance of a stock by comparing the buying price to the current stock price, computing the profit or loss, and displaying the current value of the user's holdings.

5. **Viewing Portfolio**: 
   The `view_portfolio()` function displays the user's entire portfolio, showing details for each stock such as the number of shares, the buying price, the current market price, and the total current value of the investment.

6. **Plotting Stock Prices**: 
   The `plot_stock(symbol)` function fetches stock prices at 1-minute intervals for the given symbol and plots the stock price trend over time using `matplotlib`.

7. **User Interaction**: 
   A simple menu-driven interface is provided, allowing users to interact with the portfolio by selecting options from a list of available actions (add stock, remove stock, calculate performance, etc.).

### How to Run
1. Clone the repository or download the code.
2. Install the required dependencies by running:
   ```bash
   pip install requests matplotlib
   ```
3. Run the program using Python:
   ```bash
   python stock_portfolio_tracker.py
   ```
4. Interact with the menu to manage and track your portfolio.

### Notes
- Ensure you don't exceed the API request limits set by Alpha Vantage, as free-tier users have restrictions on the number of API requests they can make per minute and per day.
- The stock price is fetched in real-time, so an internet connection is required to use this tool.
