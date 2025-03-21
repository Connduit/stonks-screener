"""
this file saves the json to a google sheet
"""


import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and authenticate using the service account key
scope = ["https://www.googleapis.com/auth/spreadsheets.readonly", "https://www.googleapis.com/auth/drive.file"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

# Authenticate and access Google Sheets
client = gspread.authorize(creds)

# Open the spreadsheet by its name or URL
#spreadsheet = client.open("stock-data")
spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1nf7ZjJNYORrNdx00XEr7n2M_cZ5q72l_phtx6mAJtgs/")

worksheet = spreadsheet.get_worksheet(0)  # Use the first sheet (index 0)

# Fetch all the data from the sheet
data = worksheet.get_all_records()

# Convert the data into JSON format (you can use this in your webpage)
import json
json_data = json.dumps(data)

# Save the data to a file for use on the webpage
# TODO: this wipes out all data in stock_data.json
with open("../data/stock_data.json", "w+") as file: # TODO: might not be able to open
    file.write(json_data)
