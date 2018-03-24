# Lucia Saura 19/03/2018
# Attempting to run the code proposed in the Euler page
# https://learnonline.gmit.ie/pluginfile.php/344250/mod_resource/content/1/euler-5-overview.pdf
# Code seem to not be python
k = 20
N = 1
i = 1
check = true
limit = sqrt(k)
while p[i]<= k
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

#Result: I get an error: 
#Ls-MacBook-Air:Week 4_13_03_2018 lucia$ python Euler5v5.py
  #File "Euler5v5.py", line 7
    #while p[i] <= k
    #^
#IndentationError: unexpected indent
