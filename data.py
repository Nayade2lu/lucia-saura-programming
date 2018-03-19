#Format Iris data Lucia Saura 19/03/2018
# working on formating Iris data (not working, error Unknown format code 'd' for object of type 'str')

with open("irisdata.csv") as f:
    contents = f.read()
    print ('{:2d} {} {} {} {}'.format(contents))

print ("out of with")
