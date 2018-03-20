#Open Iris data Lucia Saura 20/03/2018
# iris data set split in columns (from KENNETH MC TIGUE code)

with open("irisdata.csv") as f:
    for line in f:
        print ("{:>12} {:>12} {:>13} {:>12}" .format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))
       
        

