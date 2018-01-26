import logging

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
logging.basicConfig(filename='test.log',level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
num1=100
num2=10
a=add(num1,num2)
logging.debug(a)
logging.warning(sub(num1,num2))
logging.error(mul(num1,num2))
logging.critical(div(num1,num2))