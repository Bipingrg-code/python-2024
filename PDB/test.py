# importing pdb 
import pdb 

# make a simple function to debug 
def fxn(n): 
	for i in range(n): 
		print("Hello! ", i+1) 


# starting point to debug 
pdb.set_trace() 
fxn(5) 
