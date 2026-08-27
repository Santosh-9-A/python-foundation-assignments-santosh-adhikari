#Part-B Use your module together with random and datetime

import random
from datetime import datetime
import temperature_utils

# 1. Generate 5 random Celsius temperatures
celsius = []
for i in range(5):
    celsius.append(random.randint(15, 40))

# 2. Convert each to Fahrenheit
fahrenheit = []
for temp in celsius:
    fahrenheit.append(temperature_utils.celsius_to_fahrenheit(temp))

# 3. Print today's date
today = datetime.now()
print("Temperature Report -", today.strftime("%d-%m-%Y"))

# 4. Print the lists and module version
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
print("Module version:", temperature_utils.MODULE_VERSION)