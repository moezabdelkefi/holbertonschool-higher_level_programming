<h1 align="center">Classes and Objects</h1>


Class: The class is a user-defined data structure that binds the data members and methods into a single unit. Class is a blueprint or code template for object creation. Using a class, you can create as many objects as you want.

                                                        class ClassName:
                                                            # Statement

Object: An object is an instance of a class. It is a collection of attributes (variables) and methods. We use the object of a class to perform actions.
                                                        obj = ClassName()
                                                        print(obj.atrr)

## Class Attributes:

Instance variables: The instance variables are attributes attached to an instance of a class. 
We define instance variables in the constructor ( the __init__() method of a class).

Class Variables: A class variable is a variable that is declared inside of class, 
but outside of any instance method or __init__() method.

## The self

Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it

## Class Methods:

Instance method: Used to access or modify the object state. If we use instance variables inside a method, such methods are called instance methods.

Class method: Used to access or modify the class state. In method implementation, if we use only class variables, then such type of methods we should declare as a class method.

Static method: It is a general utility method that performs a task in isolation. Inside this method, we don’t use instance or class variable because this static method doesn’t have access to the class attributes.

## Object Properties

Every object has properties with it. In other words, we can say that object property is an association between name and value.

        Obj.PROPERTY = value
## getter and setter

We use getters & setters to add validation logic around getting and setting a value.
To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.

