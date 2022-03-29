import csv
import requests
import json

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp-9"

student = {
    "submitterEmail": "btan90@gmail.com", #<Your coursera account email>
    "secret": "R1wWCQrtqcTjeHW3" #<Your secret token from coursera>
}

sql1_numFilteredEntries = 189 #<The count of the filtered entries from 3.3 SQL query 1>
sql2_numFilteredEntries = 1277 #<The count of the filtered entries from 3.3 SQL query 2>

viz0CsvPath = "mp9-viz0.tsv" #<Filepath for your tableau viz0 csv/tsv file>
viz1CsvPath = "mp9-viz1.tsv" #<Filepath for your tableau viz1 csv/tsv file>
viz2CsvPath = "mp9-viz2.tsv" #<Filepath for your tableau viz2 csv/tsv file>

# The column ordering in the tsv file may not be preserved when you export the data.
# Therefore, please check and modify the respective column index below

viz0DestAirportColumn = 0 # <index of 'Destination Airport' column (0-indexed)>
viz0CountAirlineColumn = 1 # <index of 'Count of Airline' column (0-indexed)>
viz0LatitudeColumn = 2 # <index of 'Latitude' column (0-indexed)>
viz0LongitudeColumn = 3 # <index of 'Longitude' column (0-indexed)>

viz1StopOverColumn = 0 # <0 if the first column is the airport title, else 1>
viz2ArrivalDelayColumn = 0 # <0 if the first column is the arrival delay, else 1>

def readViz0(filePath, destAirportColumn, countAirlineColumn, latitudeColumn, longitudeColumn):
    vizData = {}

    with  open(filePath, encoding="utf8", errors='ignore') as csvfile:
        reader = csv.reader((line.replace('\0','') for line in csvfile), delimiter='\t')
        header = reader.__next__()

        for row in reader:
            if len(row) == 4:
                vizData[row[destAirportColumn]] = [str(row[countAirlineColumn]), str(row[latitudeColumn]), str(row[longitudeColumn])]

    return vizData

def readViz12(filePath, keyColumn):
    vizData = {}
    valueColumn = int(not keyColumn)

    with  open(filePath, encoding="utf8", errors='ignore') as csvfile:
        reader = csv.reader((line.replace('\0','') for line in csvfile), delimiter='\t')
        header = reader.__next__()

        for row in reader:
            if len(row) == 2:
                vizData[row[keyColumn]] = int(row[valueColumn])

    return vizData


def sendToAutograder(payload):
    r = requests.post(url, data=json.dumps(payload))
    print(r.status_code, r.reason)
    print(r.text)

def main():
    viz0Data = readViz0(viz0CsvPath, viz0DestAirportColumn, viz0CountAirlineColumn, viz0LatitudeColumn, viz0LongitudeColumn)
    viz1Data = readViz12(viz1CsvPath, viz1StopOverColumn)
    viz2Data = readViz12(viz2CsvPath, viz2ArrivalDelayColumn)

    payload = {}
    payload['student'] = student
    payload['sql1_numFilteredEntries'] = sql1_numFilteredEntries
    payload['sql2_numFilteredEntries'] = sql2_numFilteredEntries
    payload['viz0'] = viz0Data
    payload['viz1'] = viz1Data
    payload['viz2'] = viz2Data
    print(json.dumps(payload))
    sendToAutograder(payload)

if __name__== "__main__":
    main()