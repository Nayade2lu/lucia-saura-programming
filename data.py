#Open Iris data Lucia Saura 20/03/2018
# iris data set split in lines

with open("irisdata.csv") as f:
    for line in f:
        print(line)
        line_split=line.split(',')
        print(line.split)
       
        

