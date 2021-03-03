import csv
import pandas as pd 
with open('list.csv', 'r', encoding='Latin1') as csv_file:
    #csv_reader = csv.reader(csv_file)

    #next(csv_reader)

    df = pd.read_csv(csv_file) 
    print(df.head)



    #for line in csv_reader:
    #    print(line[0] +" | " +line[5]+" | " +line[6]+" | " +line[7]+" | " +line[8]+" | " +line[9]+" | " +line[11]+" | " +line[13])

