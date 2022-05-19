from configparser import ConfigParser
import os
import time
file = 'config.ini'
path = os.path.dirname(os.path.realpath(__file__))
configdir = '/'.join([path,'config.ini'])
config = ConfigParser()

config.read(configdir)
print('your name is ',config['client']['name'],config['client']['middlename'],config['client']['surname'])
while True:
    print('type:')
    x=input()
    y = x.split()
    num = len(y)
    if num==3:
        config.set('client','name',y[0])
        config.set('client','middlename',y[1])
        config.set('client','surname',y[2])
    if num==2:
        config.set('client','name',y[0])
        config.set('client','middlename','')
        config.set('client','surname',y[1])  
    print('your name is ',config['client']['name'],config['client']['middlename'],config['client']['surname'])
    time.sleep(5)