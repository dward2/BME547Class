# analysis.py

import calculator

seconds_in_hour = calculator.multiply(60, 60)
second_in_day = calculator.multiply(seconds_in_hour, 24)
print("There are {} seconds in a day".format(second_in_day))
