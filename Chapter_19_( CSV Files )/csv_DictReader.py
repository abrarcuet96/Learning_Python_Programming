from csv import DictReader
# ordered dict
with open('file1.csv','r') as f:
    csv_reader=DictReader(f)
    for row in csv_reader:
        print(row['name'])
        print(row['email'])