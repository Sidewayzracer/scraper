import csv
import requests
import os

# Constants for the CSV file and URL
CSV_FILE = 'json data/extracted_values.csv'
URL_TEMPLATE = 'https://www.asastats.com/static/thumbnails/{}/{}.png'

# Open the CSV file and read the data
with open(CSV_FILE, 'r') as f:
    reader = csv.reader(f)
    # Get the header row and find the index of the column we want
    headers = next(reader)
    index_col_index = headers.index('index')
    # Iterate over the remaining rows in the file
    for row in reader:
        # Get the index value from the current row
        index_value = row[index_col_index]
        # Modify the first variable in the URL using divmod() and str()
        first_var = str(divmod(int(index_value), 10000)[0] * 10000)
        # Use the modified first variable and the index value to construct the URL for the image
        url = URL_TEMPLATE.format(first_var, index_value)
        # Download the image from the URL
        response = requests.get(url)
        # Save the image to a file with the original file name
        with open('images/' + index_value + '.png', 'wb') as f:
            f.write(response.content)
