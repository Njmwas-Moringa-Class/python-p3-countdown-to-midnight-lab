# your code goes here!
from time import sleep


def countdown(f):
    x = f
    while x > 0:
        print(f"{x} SECOND(S)!")
        x -= 1
    print("HAPPY NEW YEAR!") 

def countdown_with_sleep(f):
    x = f
    while x > 0:
        sleep(1)
        print(f"{x} SECOND(S)!")
        x -= 1
    print("HAPPY NEW YEAR!") 
    
# countdown(5)