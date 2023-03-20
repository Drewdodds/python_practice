# A Module is basically a file containing a set of functions to include in your application.
#There are core modules, modules you can install using the pip package manager (including Django) as well as custom modules

import datetime
import time
from camelcase import CamelCase

today = datetime.date.today()


print(today)

timestamp = time.time()

print(timestamp)

c = CamelCase()
print(c.hump('hello there world'))