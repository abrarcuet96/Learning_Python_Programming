# csv--> comma seperated values
# use for data store(in tabuler form)

from csv import reader
with open('file1.csv','r') as f:
    csv_reader=reader(f)
    # csv_reader --> iterator
    # in iterator we can only apply loop one time.
    next(csv_reader)
    for row in csv_reader:
        print(row)