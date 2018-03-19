#Open Iris data Lucia Saura 19/03/2018
# more straight forward than the previous way with the "with" keyword

with open("irisdata.csv") as f:
    contents = f.read()
    print (contents)
print ("out of with")
