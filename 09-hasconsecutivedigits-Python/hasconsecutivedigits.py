# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	if (n<0):
		n= -n
	p = -1
 	while(n>0):
        r=n%10
    	n=n//10
     	if(r==p):
         	return True
    	p=r 
	return False