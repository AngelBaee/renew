import re 

s = 'Hey there, It is Angel, I am trying to get to know with reg ex and it is somehow going, lets see what can we do. '
pattern = 'is'

if re.search(pattern, s):
    print("Matched")
else:
    print(" Ain't ")    
