from csv import DictWriter
with open('file4.csv','w',newline='') as f:
    csv_writer=DictWriter(f,fieldnames=['first_name','last_name','age'])
    csv_writer.writeheader()
#writerow:
    # csv_writer.writerow({
    #     'first_name':'abrar',
    #     'last_name':'haider',
    #     'age':23,
    # })
    # csv_writer.writerow({
    #     'first_name':'abir',
    #     'last_name':'hossain',
    #     'age':22,
    # })

#writerows:
    csv_writer.writerows([
         {'first_name':'abrar',
         'last_name':'haider',
         'age':23},
         {'first_name':'araf',
         'last_name':'haider',
         'age':18}
    ])