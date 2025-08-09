# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.
import math
print("Enter a number:")
try:
    num = int(input())
except ValueError:
    print("Please enter a number.")
else:
    squireRoot = math.sqrt(num)
    log = math.log(num)
    sin = math.sin(num)
    print("square root:", squireRoot)
    print("logarithm:", log)
    print("sin:", sin)



