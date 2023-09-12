import random

x=random.randint(1,1000)

random.seed(x)
print(random.random())

random.seed(x)
print(random.random())