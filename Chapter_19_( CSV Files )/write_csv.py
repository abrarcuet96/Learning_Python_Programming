# writer, DoctWriter
from csv import writer
with open('file3.csv','w',newline='') as f:
    csv_writer=writer(f)
# two methods--> writerow,writerows
# writerow:
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['Abrar','Bangladesh'])
    # csv_writer.writerow(['Abir','America'])

# writerows:
    csv_writer.writerows([['name','country'],['Abrar','Bangladesh'],['Abir','America']])