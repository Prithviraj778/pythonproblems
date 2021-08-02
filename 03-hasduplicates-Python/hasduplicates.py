# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
    # your code goes here
    t=[]
    for i in L:
        for j in i:
            t.append(j)
    for i in range(len(t)):
        for j in range(i+1,len(t)):
            if (t[i]==t[j]):
                return True
      
    return False