# author: zzq

import time

x = time.localtime(123213123)

print(x)

print(x.tm_year)

print('this is 1973 day: %d' %x.tm_yday)

time.strptime()