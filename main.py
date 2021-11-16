# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

# part 1


import time
import math
import datetime
import sys
from greet import supergreeting

# part 2

def wait(seconds:int):
    time.sleep(seconds)
    return None


# part 3

def my_sin(num:float):
    return math.sin(num)



# part 4

def iso_now():
    return datetime.datetime.now().isoformat()



# part 5

def platform():
   return sys.platform


# part 6

def supergreeting_wrapper(name):
    return supergreeting(name)

print(wait(1))
print(my_sin(45))
print(iso_now())
print(platform())
print(supergreeting_wrapper("Bob"))