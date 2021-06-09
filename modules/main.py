# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
import time
import this
import math
import datetime
import sys
from greet import supergreeting

def wait(seconds):
    time.sleep(seconds)
    return 0  

def my_sin(x):
    answer = math.sin(x)
    return answer

def iso_now():
    nu = datetime.datetime.now()
    nu_formatted = nu.strftime("%Y-%m-%dT%H:%M")
    return nu_formatted
    
def platform():
    return sys.platform

def supergreeting_wrapper(name):
    return supergreeting(name)












