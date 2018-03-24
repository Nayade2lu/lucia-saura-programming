# Lucia Saura 19/03/2018
# Attempting to run the code proposed in the Euler page adding the Prime numbers each one of them for a p[] position
# https://learnonline.gmit.ie/pluginfile.php/344250/mod_resource/content/1/euler-5-overview.pdf
# Code seem to not be python
k = 20
N = 1
i = 1
p[1]=2
p[2]=3
p[3]=5
p[4]=7
p[5]=11
p[6]=13
p[7]=17
p[8]=19
check = true
limit = sqrt(k)

    while p[i] <= k:
        a[i] = 1
        if check then
            if p[i] <= limit then
                a[i] = floor( log(k) / log(p[i]) )
            else
                check = false
            end if
        end if
        N = N * p[i] ^ a[i]
    i = i + 1
end while 
output N

#Getting the same error as the code seem not to be python
#Ls-MacBook-Air:Week 4_13_03_2018 lucia$ python Euler5v5.py
  #File "Euler5v5.py", line 15
    #while p[i] <= k:
    #^
#IndentationError: unexpected indent
