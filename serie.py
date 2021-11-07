def serie(x , n):
    if n > len(x):
        print ("Invalid length")
    else:               
        for i in range(len(x)):
            if len(x[i:i+n]) == n:
                print (x[i:i+n])
x = 49142
n = 3
serie(str(x), n)