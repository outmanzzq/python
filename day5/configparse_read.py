# author: zzq

import configparser

config = configparser.ConfigParser()

config.read('example.ini')
print(config.sections())

