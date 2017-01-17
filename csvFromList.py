import csv

# write from records list to csv file
def writeToCSV(fileName, recordsList):
    with open(fileName, 'w',  newline='') as csvfile:
        writer = csv.writer(csvfile,  delimiter=',', quotechar = '"', quoting = csv.QUOTE_ALL)
        for tuple in recordsList:
            writer.writerow(tuple)
    csvfile.close()

#read from csv file and print to standard output
def readFromCSV(fileName):
    with open(fileName,  newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            print(row)
    csvfile.close()

#input list of tuples
records = [('column1','column2','column3','colum4'),
         ('aaaaaaa','bbbbbbb','ccccccc','dd\'dd"dd,d'),
         ('\'eeeeeee\'','"fffffff"','gg"gggg"g','hh?!@h#$%^&*('),
         ('     _a','     ','null','NULL'),
         (1234567,'5565.234','..67837','abce123')]

writeToCSV('/home/hanshika/Desktop/aaaaaaa.csv',records)
readFromCSV('/home/hanshika/Desktop/aaaaaaa.csv')

