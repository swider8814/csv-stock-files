import urllib.request
import csv

# list of URLs to CSV files
urls = [""]

# columns header in output file
header = ["product_code", "stock"]

# empty list to which we will add data from each CSV file
data = []

# downloading and adding data from CSV files to the date list
for url in urls:
    response = urllib.request.urlopen(url)
    lines = [l.decode("cp1250") for l in response.readlines()]
    reader = csv.reader(lines, delimiter=";")
    for row in reader:
        if row[1] != '' and row[2] != '':
            data.append([row[0], row[1]])

# summary of stock values for each product_code
result = {}
for row in data:
    code = row[0]
    stock = row[1]
    if code not in result:
        result[code] = 0
    try:
        stock = int(stock)
    except ValueError:
        continue
    result[code] += stock

# saving results to CSV file
with open("stock.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(header)
    for code, stock in result.items():
        writer.writerow([code, stock])
