#Random Quote Generator Python 

#import quote & random = 
from quote import quote 

import random 

#Main Body / Section of the code =
print("Enter the name of your favorite author / person")

q_author = input()

quotes = quote(q_author)

quote_no = random.randint(1,len(quotes))

#Output of the code =
print("Author: ",quotes[quote_no]['author'])

print("->", quotes[quote_no]['quote'])
