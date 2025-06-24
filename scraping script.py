import json
import csv


# Open the JSON file and load the data
with open('json data/godrones creator assets.json', 'r') as f:
    json_data = json.load(f)

# Open the output file in write mode
with open('json data/extracted_values.csv', 'w', newline='') as out_file:
    # Create a CSV writer object
    csv_writer = csv.writer(out_file)

    # Write the column headers to the CSV file
    csv_writer.writerow(['index', 'unit_name', 'url'])

    # Iterate through the assets in the JSON object
    for asset in json_data['assets']:
        # Extract the index, unit-name, and url values
        index = asset['index']
        unit_name = asset['params'].get('unit-name', 'N/A')
        url = asset['params'].get('url', 'N/A')

        # Write the values to the CSV file
        csv_writer.writerow([index, unit_name, url])