import csv

input = [('\'app,le\' r,e\'d','b','c','d'),('e','f','g','h'),('i','j','k','l'),('m','n','o','p'),('q','r','s','t'),('u','v','w','x')]

with open('/home/hanshika/Desktop/aaaaaaa.csv', 'w',  newline='') as csvfile:
    writer = csv.writer(csvfile,  delimiter=',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
    for tuple in input:
        writer.writerow(tuple)
csvfile.close()

with open('/home/hanshika/Desktop/aaaaaaa.csv',  newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        print(','.join(row))


