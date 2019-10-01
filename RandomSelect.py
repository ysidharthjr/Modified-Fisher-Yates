import random

def randomSelect(a,N):
    L=len(a)                       #Lenght of entire array
    for i in range(L-1,L-N-1,-1):  #Running the loop from last index(L-1) to Nth last index (L-N)
        ch=random.randrange(i+1)   #Randomly Generating a Number in range 0<= ch <=i
        a[i],a[ch]=a[ch],a[i]      #Exchanging the ith and randomly selected index in range 0-i
        
    return a[L-N:]                 #Only returning the last N elements of the list


#For testing the function
ar=[3,5,9,34,67,234,7,423,677]
        
randomSelect(ar,4)

#Line 5 and 9 are modified from Fisher-Yates shuffling algorithm
