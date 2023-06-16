import tkinter as tk
from tkinter import messagebox, ttk
from forex_python.converter import CurrencyRates
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initialize the currency converter
c = CurrencyRates()

class StockDataTracker(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Stock Data Tracker")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.symbol_label = tk.Label(self, text="Stock Symbol:")
        self.symbol_label.grid(row=0, column=0, sticky="e")
        self.symbol_entry = tk.Entry(self)
        self.symbol_entry.grid(row=0, column=1, sticky="w")

        self.start_date_label = tk.Label(self, text="Start Date (YYYY-MM-DD):")
        self.start_date_label.grid(row=1, column=0, sticky="e")
        self.start_date_entry = tk.Entry(self)
        self.start_date_entry.grid(row=1, column=1, sticky="w")

        self.currency_label = tk.Label(self, text="Currency:")
        self.currency_label.grid(row=2, column=0, sticky="e")

        self.currency_combo = ttk.Combobox(self, values=CurrencyCode_list)
        self.currency_combo.grid(row=2, column=1, sticky="w")
        self.currency_combo.set("Select Currency")

        self.submit_button = tk.Button(self, text="Get Data", command=self.fetch_stock_data)
        self.submit_button.grid(row=3, columnspan=2)

        # Create a Figure object and a corresponding FigureCanvasTkAgg widget
        self.figure = plt.Figure(figsize=(8, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().grid(row=4, columnspan=2)

    def fetch_stock_data(self):
        symbol = self.symbol_entry.get()
        start_date_str = self.start_date_entry.get()
        currency = self.currency_combo.get()
        
        from forex_python.converter import CurrencyRates
        c = CurrencyRates()

        if symbol and start_date_str and currency != "Select Currency":
            try:
                start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
                end_date = datetime.now()

                # Download stock data
                data = yf.download(symbol, start=start_date, end=end_date)
                close_prices = data['Close']

                # Convert currency
                to_currency = currency
                from_currency = "USD"  # Converting to USD for the Y-axis
                conversion_rate = c.convert(from_currency, to_currency, 1)  # Conversion rate for 1 unit of from_currency to to_currency

                # Apply currency conversion to the closing prices
                close_prices_converted = close_prices * conversion_rate
                
                # Find the indices and values of the highest and lowest closing prices
                max_index = close_prices_converted.idxmax()
                max_value = close_prices_converted[max_index]
                min_index = close_prices_converted.idxmin()
                min_value = close_prices_converted[min_index]
                
                # Clear the previous plot
                self.figure.clear()

                # Plot the converted closing prices on the Figure
                axis = self.figure.add_subplot(111)
                
                axis.plot(close_prices_converted)
                
                # Get the currency symbol
                currency_symbol = currency_symbols.get(currency)

                # Highlight the highest and lowest closing prices with symbols
                axis.scatter(
                    max_index,
                    max_value,
                    color='red',
                    label=f'Highest: {currency_symbol}{max_value:.2f} ({max_index.date()})'
                )
                axis.scatter(
                    min_index,
                    min_value,
                    color='green',
                    label=f'Lowest: {currency_symbol}{min_value:.2f} ({min_index.date()})'
                )
                axis.set_xlabel('Date')
                axis.set_ylabel(f'Closing Price ({to_currency})')  # Update the Y-axis label
                axis.set_title(f'{symbol} Stock Price')
                axis.grid(True)

                # Add a legend
                axis.legend()

                # Redraw the FigureCanvasTkAgg widget
                self.canvas.draw()

            except Exception as e:
                print(f"Error occurred while fetching data: {str(e)}")
        else:
            print("Please enter a stock symbol, a valid start date (YYYY-MM-DD), and select a currency.")


CurrencyCode_list = [
    "INR", "USD", "CAD", "CNY", "DKK", "EUR", "GBP", "JPY", "AUD", "NZD",
    "CHF", "SEK", "NOK", "BRL", "RUB", "TRY", "KRW", "HKD", "SGD", "MYR",
    "THB", "IDR", "PHP", "ZAR", "MXN"
]

currency_symbols = {
    "INR": "₹",
    "USD": "$",
    "CAD": "C$",
    "CNY": "¥",
    "DKK": "kr",
    "EUR": "€",
    "GBP": "£",
    "JPY": "¥",
    "AUD": "A$",
    "NZD": "NZ$",
    "CHF": "Fr",
    "SEK": "kr",
    "NOK": "kr",
    "BRL": "R$",
    "RUB": "₽",
    "TRY": "₺",
    "KRW": "₩",
    "HKD": "HK$",
    "SGD": "S$",
    "MYR": "RM",
    "THB": "฿",
    "IDR": "Rp",
    "PHP": "₱",
    "ZAR": "R",
    "MXN": "Mex$",
}

root = tk.Tk()
app = StockDataTracker(master=root)
app.mainloop()
