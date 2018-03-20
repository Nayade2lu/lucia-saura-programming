#Open Iris data Lucia Saura 20/03/2018
# iris data set split in columns (based on SARAH SCHOLZ code)
# 

with open("irisdata.csv") as f:
    for line in f: #loops trough each line
        print('{:6} {:6} {:6} {:6}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]), line.split(',')[4])
        # first bit are the spaces between columns, second bit spliting and formating every colum
        # added the last part to show the text column as well
       
        

