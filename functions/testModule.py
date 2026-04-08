# notice: create a module to be able to use functions from a different file
import functions2 as f
print(f.calculate(6, 2))
# notice: to abbreviate a file's name, use 'as'

# notice: to import one specific function, use 'from'
from functions2 import mltpSquare
print(mltpSquare(5, 6))