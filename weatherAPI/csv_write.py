import csv

filename = "weather_data.csv"

fields = ['Date Added','Time','Wind Speed(MPH)', 'Wind Direction', 'Rain Chance(%)']
rows = [['10/10/21','4:30PM', '2', 'NW', '10'],
        ['10/11/21','5:20PM', '3' ,'S', '5']
        ]

'''
with open(filename, 'a') as csvfile: #open file
    csvwriter = csv.writer(csvfile)
    
    csvwriter.writerow(fields)  #write in fields 
    csvwriter.writerows(rows)   #write in rows
'''
def csv_input(input):
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(input)

