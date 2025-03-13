import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and authenticate using the service account key
scope = ["https://www.googleapis.com/auth/spreadsheets.readonly", "https://www.googleapis.com/auth/drive.file"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

# Authenticate and access Google Sheets
client = gspread.authorize(creds)

# Open the spreadsheet by its name or URL
spreadsheet = client.open("stock-data")
worksheet = spreadsheet.get_worksheet(0)  # Use the first sheet (index 0)

# Fetch all the data from the sheet
data = worksheet.get_all_records()

# Convert the data into JSON format (you can use this in your webpage)
import json
json_data = json.dumps(data)

# Save the data to a file for use on the webpage
with open("stock_data.json", "w") as file:
    file.write(json_data)
