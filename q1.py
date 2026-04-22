class StringContainer:
    """
    A class that stores a string. Has print option.
    """
    def get_String(self, input):
        """
        Gets the string input and stores it in the class.
        """
        self.input = input
        return self.input

    def print_String(self):
        """
        Prints the stored string in uppercase.
        """
        print(self.input.upper())

    def __str__(self):
        return self.input


data = StringContainer()
data.get_String("hello world?")
data.print_String()
