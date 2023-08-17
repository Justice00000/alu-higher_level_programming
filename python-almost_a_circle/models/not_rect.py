#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes of the object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # List of getter functions
    @property
    def width(self):
        """Gets the value for width"""
        return self.__width

    @property
    def height(self):
        """Gets the value for height"""
        return self.__height

    @property
    def x(self):
        """Gets the value for x"""
        return self.__x

    @property
    def y(self):
        """Gets the value for y"""
        return self.__y
    
    # list of setter functions
    @width.setter
    def width(self, value):
        """sets the value for width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """sets the value for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if x <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if y <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value
