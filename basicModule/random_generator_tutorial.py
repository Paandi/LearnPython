#random_number_generator

--Range
for i in range(0,20,2):
	print(i)
	
--Random

import random

x=[1,2,3,4,5,29,30,12,9]

for i in range(0,20,2):                       --- to pick random item from a list
	print(random.choice(x))
	

random.randint(1,3)                           --- to pick from a integer range 
random.random()                               --- 0 to 1 floating   
