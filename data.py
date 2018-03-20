#Open Iris data Lucia Saura 20/03/2018
# iris data set split in columns (from SARAH SCHOLZ code)
# Now I am ony missing  how to print the text (strings)

with open("irisdata.csv") as f:
    for line in f:
        print('{:5} {:5} {:5} {:5}'.format(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3]))
        # first bit are the spaces between columns, second bit spliting and formating every colum
       
        

