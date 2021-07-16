# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.


def frequent(x,n):
    counter=0
    while (n!=0):
        if n%10==x:
            counter+=1
        n=n//10
    return counter


def mostfrequentdigit(n):
    big=0
    for i in range (10):
        if frequent(i,n)>frequent(big,n):
            big=i
    return big
	# your code goes here
	