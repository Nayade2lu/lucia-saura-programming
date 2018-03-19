#Open Iris data Lucia Saura 19/03/2018
# more straight forward than the previous way with the "with" keyword

with open("irisdata.csv") as f:
    for line in f:
        print(line.split (',') , [1])

print ("out of with")
