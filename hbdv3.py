import ascii_magic
import threading
import time
from random import randint
# from hbdcp import cphbd
my_art = ascii_magic.from_image_file('2.jpg',char='#')
# ascii_magic.to_terminal(my_art)
# print(my_art)
my_wish = ascii_magic.from_image_file('5.jpg' ,back=ascii_magic.Back.BLACK ,char='#')
# print(my_wish)
my_cake = ascii_magic.from_image_file('cake4.jpg',char='#')


# def task1():
    
#     for letter in my_cake:
#         time.sleep(0.00031)
#         print(letter,end='')
        
def task2() :   
    for letter in my_cake:
        time.sleep(0.00021)
        print(letter,end='')
    for letter in my_wish:
        time.sleep(0.00021)
        print(letter, end='')
  
    for letter in my_art:
        time.sleep(0.00021)
        print(letter, end='')


# t1 = threading.Thread(target=task1, name='t1')
t2 = threading.Thread(target=task2, name='t2')
        

# celebrate()
# play1=cphbd()
# play1.cpclass()
# t1.start()
t2.start()
