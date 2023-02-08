#Must include this in order to use the cmu_graphics library
from cmu_graphics import *

"""
Here's where you can write your own code. Below I've created a black background with white rectangle.
"""
app.background = 'black'

Rect(200, 200, 10, 10, fill='white', align="center")

# Must include in order to run your file. Think of this as the run button
cmu_graphics.run()