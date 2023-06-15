import tkinter as tk
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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

        self.submit_button = tk.Button(self, text="Get Data", command=self.fetch_stock_data)
        self.submit_button.grid(row=2, columnspan=2)

        # Create a Figure object and a corresponding FigureCanvasTkAgg widget
        self.figure = plt.Figure(figsize=(8, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().grid(row=3, columnspan=2)

    def fetch_stock_data(self):
        symbol = self.symbol_entry.get()
        start_date_str = self.start_date_entry.get()

        if symbol and start_date_str:
            try:
                end_date = datetime.today()
                start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

                data = yf.download(symbol, start=start_date, end=end_date)
                close_prices = data['Close']

                # Clear the previous plot
                self.figure.clear()

                # Plot the closing prices on the Figure
                axis = self.figure.add_subplot(111)
                axis.plot(close_prices)
                axis.set_xlabel('Date')
                axis.set_ylabel('Closing Price')
                axis.set_title(f'{symbol} Stock Price')
                axis.grid(True)

                # Redraw the FigureCanvasTkAgg widget
                self.canvas.draw()

            except Exception as e:
                print(f"Error occurred while fetching data: {str(e)}")
        else:
            print("Please enter a stock symbol and a valid start date (YYYY-MM-DD).")


root = tk.Tk()
app = StockDataTracker(master=root)
app.mainloop()
