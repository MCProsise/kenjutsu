
import logging
logging.basicConfig(level=logging.DEBUG)
def squared_threes():
    return_value = []
    
    for num in range(0,100):
        if num % 3 == 0:
            square = num ** 2
            print(square)

    return return_value
if __name__ == "__main__":
   for x in squared_threes():
       print(x)