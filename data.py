#Format Iris data Lucia Saura 19/03/2018
# working on formating Iris data (not working, error <_io.TextIOWrapper name='irisdata.csv' mode='r' encoding='UTF-8'>)

with open("irisdata.csv") as f:
    contents = f.read()
    print(repr(f).rjust(2))
    

print ("out of with")
