from csv import DictReader
# ordered dict
with open('file2.csv','r') as f:
    csv_reader=DictReader(f,delimiter='|')
    for row in csv_reader:
        print(row['name'])
        print(row['email'])