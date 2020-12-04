import logging
import json
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

# last = "I am very young"
# second = "I am very old"
# logging.debug(f"Matt said that {last}. Vicky said that {second}.")

# cars = ["bmw", "mercedes", "lamborghini"]
# logging.debug(cars[-1])
# logging.debug(cars)


#x = range(20)
#numbers = list(x)
#numbers = list(range(20))
#logging.debug(numbers)

#squares = [value ** 2 for value in range(20)]
#logging.debug(squares)


# def squared_threes():
#     return_value = []
    
#     for value in range(0, 100):
#         if value % 3 == 0:
#             value = value ** 2
#             return_value.append(value)
        

#     return return_value
# if __name__ == "__main__":
#     for x in squared_threes():
#         print(x)    

# cars = ['bmw', 'subaru', 'gmc', 'ram']
# for car in cars:
#     if car != 'subaru':
#         print(car.upper())
#     else:
#         print(car.title())    


# print('What is the name of your car?')
# mycar = input()
# print(f'The name of your car is {mycar}.')
#--------------------

# d = {'house' : 'bungalow', 'school' : 'Walnut Hill'}
# d['grade'] = '3rd'
# x = d.get('school')
# print(x)
#print(d)

# countries = {'usa': 'washington dc', 'russia' : 'moscow'}
# print(countries)
#----------------------

# def fib(n):
#     first = 0
#     second = 1
#     for x in range(n):
#         print(first)
#         first, second = second, first+second
# if __name__ == "__main__":
#     logging.debug("Calling fib(3)")
#     fib(3)
#     logging.debug("Calling fib(8)")
#     fib(8)
#---------------------

# planets = []
# planets.append({'Earth' : '3rd'})
# print(planets)
#---------------------

# while True:
#     try:
#         x = int(input('Please enter a number: '))
#         break
#     except:
#         print('Oops! That was no valid number. Try again...')

#While loop will continue until user input is correct.
#When user input is an integer the while loop will terminate.

# x = 0 ** 0
# print(x)


# def get_sum(incoming):
#     retval = 0
    
    
    
#     return retval
    
# if __name__ == "__main__":
#     my_text = """
#     zi8LKk3tqBt5qBYrXKPu
#     H6Sqfwba6sRe3D8OjbOp
#     HgPjXjrKBqIvPqt9rT0J
#     emRRMr1pt5332sHN1GkZp
#     8IA8JMmMMCYyuu7Ncfai
#     wkJxoiwfiX7wunLRZCxa
#     GgSssxOpQ4345w81TSKB
#     WGnmR2MnKXuUvz4X6ERr 
#     """ 
#     print(get_sum(my_text))

# def fooBar(n):
    
#     for x in range(n):
#         if x % 3 == 0:
#             print('Foo')
#         elif x % 5 == 0:
#             print('Bar')
#         elif x % 3 == 0 & x % 5 == 0:
#             print('FooBar')
#         else:           
#             print(x)

# if __name__ == "__main__":
    
#     n = input('Please enter a value: ')
#     print(fooBar(n))     



def get_odds(my_list):  
    
    i = 0
    for y in my_list:
        i + 1
        if i % 2 != 0:
            print(y)
        

if __name__ == "__main__":

    i = 0
    my_list = ['python', 'apple', 'train', 'computer', 'music']
    print(get_odds(my_list))    

