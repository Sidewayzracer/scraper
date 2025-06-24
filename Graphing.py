import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime
# Specify the URL and parameters for the API request

api_url = "https://api.coingecko.com/api/v3/coins/algorand/market_chart"
api_params = {
    "vs_currency": "usd",
    "days": 30,
    "interval": "hour",
}

# Send the API request and retrieve the response
api_response = requests.get(api_url, params=api_params).text

# Parse the JSON response
response_data = json.loads(api_response)


# Extract the data points from the response
dates = [datapoint[0] for datapoint in response_data["prices"]]
# Convert the timestamps to the 'day/hour' format
converted_dates = []
for timestamp in dates:
    date = datetime.fromtimestamp(timestamp/1000).strftime('%m/%d/%y/%H')
    converted_dates.append(date)

prices = [datapoint[1] for datapoint in response_data["prices"]]



# Get the starting price
start_price = prices[0]

# Initialize the color list
colors = []

# Iterate over the prices and add a color for each point
for price in prices:
    if prices[-1] > start_price:
        color = "green"
    else:
        color = "red"


# Set the chart background color to black
plt.style.use("dark_background")

# Add a title and axis labels
plt.title("Price of Algorand")
plt.xlabel("Date")
plt.ylabel("Price (USD)")

# Plot the data with the specified colors
plt.plot(converted_dates, prices, color=color)

# Set the x-axis tick labels to display every 7th day
plt.xticks(converted_dates[::])


# Show the plot
plt.savefig("charts/algorand_prices_30days.png", dpi=100)
plt.close()