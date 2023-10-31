# Import definition of pi
import math

# Give the user a nice message to ask for the diameter
print("Please enter a value for diameter:")

# Collect diameter from user input (called diameter)
# Charlie's Dad showed him try / except**
try:
    diameter = float(input())
except Exception as e:
    print("Invalid diameter entered!", e)
    exit()
# Make sure the input is a number and greater than zero
if diameter < 0:
    print("diameter must be a positive number!")
else:
    # Calculate radius (diameter / 2)
    radius = diameter / 2
    # Calculate the area (A = pi ** 2)
    area = math.pi * (radius ** 2)
    # Calculate the circumference (C = 2 * pi * radius)
    circumference = math.pi * diameter
    # Print a nice message for Area with the value of A
    print(
        "The value of the Area of the circle with diameter",
        diameter,
        "is",
        area,
        )
    # Print a nice message for the Circumstances with the value of C
    print(
        "The value of the Circumference of the circle with diameter",
        diameter,
        "is",
        circumference,
        )
