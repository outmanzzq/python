# author: zzq

import shelve
import datetime

d = shelve.open('shelve_test')

print(d.get("name"))
print(d.get("info"))
print(d.get("date"))

# info = {'age': 22, "job": 'IT'}
#
# name = ["alex", "rain", "test"]
# d["name"] = name
# d["info"] = info
# d["date"] = datetime.datetime.now()

d.close()