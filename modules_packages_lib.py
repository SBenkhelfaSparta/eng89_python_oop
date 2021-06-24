# pythons extensive documentation on python.org
# have used functions we created as well as built in

# import is keyword used to import any available python modules

# math
# import math # imports whole class
# from random import random # imports specific file from class
#
# num1 = 23.44 # float
#
# # have to round figure depending on value
# # if value is less the .50 round down, if .50 or above round up
#
# print(math.ceil(num1)) # rounds up to next integer
# print(math.floor(num1)) # rounds down to next integer
# print(math.pi)
#
# # if specific file is imported it doesn't need to be called from class
# print(random()) # random number between 0 and 1 everytime it is run

# how can we interact with machine using python
import os # used to get information about your OS
import datetime, sys # sys is used to get system specific info

# work_dir = os.getcwd() # provides current location/path
# print(work_dir)
# print(os.getuid()) # user id
# print(os.cpu_count()) # reads hardware info - counts CPUs of machine
# print(os.uname()) # username

# print(datetime.date.today()) # today's date
# print(sys.path) # absolute path

import requests # installed via pip console method first

requests_api = requests.get("https://www.bbc.co.uk/")
print(requests_api.status_code) # 200 for success, 404 and above for fail/unavailable
print(requests_api.headers)
print(requests_api.content)