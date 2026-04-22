class Rectangle:
    """
    A class representing a rectangle.
    """
    def __init__(self, length, width):
        """
        Initialise the rectangle with length and width.
        Throws error if length or width is not positive.
        """

        if (not isinstance(length, (int, float))
                or not isinstance(width, (int, float))):
            raise TypeError("Length and width must be numbers.")

        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")

        self.length = length
        self.width = width

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.length * self.width


rectangle = Rectangle(5, 3)
print("Area of the rectangle:", rectangle.area())
