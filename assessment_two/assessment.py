"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

2. What is a class?

3. What is a method?

4. What is an instance in object orientation?

5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

"""


# Part 2: Road Class
# #############################################################################

# Create your Road class here

# Instantiate Road objects here


# Part 3: Update Password
# #############################################################################
class User(object):
    """A user object."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # write the update_password method here


# Part 4: Build a Library
# #############################################################################
class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create your Library class here


# Part 5: Rectangles
# #############################################################################

class Rectangle(object):
    """A rectangle object."""

    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the rectangle's area (length * width)."""
        return self.length * self.width


# Create the Square class here


