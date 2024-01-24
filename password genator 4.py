# import random
import random

# gather our characters
lower= "abcdefghijklmnopqrstuvwxyz"
upper= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="{}?@!$%^&()_+"
all=lower+upper+numbers+symbols
Length=int(input())
Password=""

for i in range(Length):    
  Password+=random.choice(all)
print(Password)