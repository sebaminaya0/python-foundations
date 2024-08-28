import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Side bar
# Table of contents
st.sidebar.title("Table of Contents")

# Subpages
subpages = ["Introduction", "Data Types", "Control Structures", "Functions", "Classes", "Modules", "Packages", "File I/O"]

# Radio button
# Select the subpage
# Default is Introduction
subpage = st.sidebar.radio("Go to", subpages, index=0)

# Introduction
if subpage == "Introduction":
    init_index = 0

    st.markdown("# Welcome to Python Introduction!")
    # Display as quote
    st.markdown("> Python is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be highly readable. It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages.")
    st.markdown("> Python has gained popularity over the years and has also been used in various fields such as data science, machine learning, web development, etc. Learning Python is a must for anyone who wants to get into these fields.")

    st.markdown("## Why Python?")
    st.markdown("- Easy to learn")
    st.markdown("- Open-source")
    st.markdown("- Large community")

    st.markdown('## Python Installation')
    st.markdown('1. Go to [Python official website](https://www.python.org/downloads/)')
    st.markdown('2. Download the latest version of Python')
    st.markdown('3. Run the installer')
    st.markdown('4. Check the box "Add Python to PATH"')
    st.markdown('5. Click "Install Now"')

    st.markdown('> To check if Python is installed, open the command prompt and type `python --version`')
    st.markdown('> For further information, please refer to the [official Python documentation](https://docs.python.org/3/tutorial/index.html)')

    st.markdown('# Python Introduction')

    st.markdown('## Operations')

    st.markdown('Python supports the following operations:')

    st.markdown('1. Arithmetic operators')
    st.markdown('''
        ```python
    2 + 3 = 5 # Addition
    2 - 3 = -1 # Subtraction
    2 * 3 = 6 # Multiplication
    2 / 3 = 0.6666666666666666 # Division
    2 % 3 = 2 # Modulus
    2 ** 3 = 8 # Exponentiation
    2 // 3 = 0 # Floor division
    ''')

    st.markdown('2. Comparison operators')
    st.markdown('''
        ```python
    2 == 3 # Equal
    2 != 3 # Not equal
    2 > 3 # Greater than
    2 < 3 # Less than
    2 >= 3 # Greater than or equal to
    2 <= 3 # Less than or equal to
    ''')

    st.markdown('## Variables')

    st.markdown('Variables are used to store data values. Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.')

    st.markdown('''
        ```python
    x = 5
    y = "Hello, World!"
    ```
    ''')

    st.markdown('Variables can also be defined in one line:')

    st.markdown('''
        ```python
    x, y, z = 5, "Hello, World!", 10.5
    ```
    ''')
elif subpage == "Data Types":
    st.markdown("# Data Types")
    st.markdown("## Python Data Types")
    st.markdown("Python has the following data types:")
    st.markdown("1. Text Type: str")
    st.markdown("2. Numeric Types: int, float, complex")
    st.markdown("3. Sequence Types: list, tuple, range")
    st.markdown("4. Mapping Type: dict")
    st.markdown("5. Set Types: set, frozenset")
    st.markdown("6. Boolean Type: bool")
    st.markdown("7. Binary Types: bytes, bytearray, memoryview")

    st.markdown("## Getting the Data Type")
    st.markdown("You can get the data type of any object by using the `type()` function:")

    st.markdown('''
        ```python
        type("Hello, World!") # str
        type(10) # int
        type(10.5) # float
        type(1 + 2j) # complex
        type([1, 2, 3]) # list
        type((1, 2, 3)) # tuple
        type(range(6)) # range
        type({"name": "John", "age": 36}) # dict
        type({"apple", "banana", "cherry"}) # set
        type(frozenset({"apple", "banana", "cherry"})) # frozenset
        type(True) # bool
        type(b"Hello") # bytes
        type(bytearray(5)) # bytearray
        type(memoryview(bytes(5))) # memoryview
        ```
        ''')

elif subpage == "Control Structures":
    st.markdown("# Control Structures")
    st.markdown("## Python Control Structures")
    st.markdown("Python supports the following control structures:")

    st.markdown("1. Conditional Statements")
    st.markdown("2. Loops")

    st.markdown("## Conditional Statements")
    st.markdown("Python supports the following conditional statements:")

    st.markdown("1. if statement")
    st.markdown("2. if-else statement")
    st.markdown("3. if-elif-else statement")

    st.markdown("## Loops")
    st.markdown("Python supports the following loops:")

    st.markdown("1. for loop")
    st.markdown("2. while loop")

    st.markdown("## Examples")
    st.markdown("### if statement")

    st.markdown('''
        ```python
        x = 10
        if x > 5:
            print("x is greater than 5")
        ```
        ```terminal
        x is greater than 5
        ```
        ''')

    st.markdown("### if-else statement")

    st.markdown('''
        ```python
        x = 4
        if x > 5:
            print("x is greater than 5")
        else:
            print("x is less than or equal to 5")
        ```
        ```terminal
        x is less than or equal to 5
        ```
        ''')

    st.markdown("### if-elif-else statement")

    st.markdown('''
        ```python
        x = 5
        if x > 5:
            print("x is greater than 5")
        elif x == 5:
            print("x is equal to 5")
        else:
            print("x is less than 5")
        ```
        ```terminal
        x is equal to 5
        ```
        ''')

    st.markdown("### for loop")

    st.markdown('''
        ```python
        for i in range(5):
            print(i)
        ```
        ```terminal
        0
        1
        2
        3
        4
        ```
        ''')

    st.markdown("### while loop")

    st.markdown('''
        ```python
        i = 0
        while i < 5:
            print(i)
            i += 1
        ```
        ```terminal
        0
        1
        2
        3
        4
        ```
        ''')

elif subpage == "Functions":
    st.markdown("# Functions")
    st.markdown("## Python Functions")
    st.markdown("A function is a block of code that only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.")

    st.markdown("## Built-in Functions")
    st.markdown("Python has a set of built-in functions that you can use without importing any module.")

    st.markdown("## Examples")

    st.markdown('''
        ```python
        print("Hello, World!") # This is a built-in function that prints "Hello, World!"
        type("Hello, World!") # This is a built-in function that returns the data type of the object
        sum([1, 2, 3, 4, 5]) # This is a built-in function that returns the sum of the elements in the list
        ```
        ''')

    st.markdown("## Creating a Function")
    st.markdown("In Python, a function is defined using the `def` keyword.")

    st.markdown('''
        ```python
        def my_function():
            print("Hello, World!")
        ```

        To call a function, use the function name followed by parentheses:

        ```python
        my_function()
        ```
        ''')

    st.markdown("## Arguments")
    st.markdown("Information can be passed into functions as arguments.")

    st.markdown('''
        ```python
        def my_function(name):
            print("Hello, " + name)

        my_function("John")
        my_function("Jane")
        my_function("Doe")
        ```
        ''')

    st.markdown("## Return Values")
    st.markdown("A function can return data as a result.")

    st.markdown('''
        ```python
        def my_function(x):
            return 5 * x

        print(my_function(3)) # 15
        print(my_function(5)) # 25
        print(my_function(9)) # 45
        ```
        ''')

    st.markdown("## Default Parameter Value")

    st.markdown("The following example shows how to use a default parameter value.")

    st.markdown('''
        ```python
        def my_function(country = "Norway"):
            print("I am from " + country)

        my_function("Sweden") # I am from Sweden
        my_function("India") # I am from India
        my_function() # I am from Norway
        ```
        ''')

    st.markdown("## Good Practices")

    st.markdown("1. Function names should be lowercase, with words separated by underscores as necessary to improve readability.")
    st.markdown("2. Always use a return statement in a function.")
    st.markdown("3. Use default parameter values to improve readability.")
    st.markdown("4. Use keyword arguments to improve readability.")
    st.markdown("5. Use `*args` and `**kwargs` to accept any number of arguments.")
    st.markdown("6. Use docstrings to document the function.")
    st.markdown("7. Use type hints to improve readability.")
    st.markdown("8. Use assertions to check the input.")

    st.markdown("## Example")

    st.markdown('''
        ```python
        def add(x: int, y: int) -> int:
            """
            This function adds two numbers.
            x: int: The first number.
            y: int: The second number.
            """
            assert isinstance(x, int), "x must be an integer"
            assert isinstance(y, int), "y must be an integer"
            return x + y

        print(add(3, 5)) # 8
        ```
        ''')

elif subpage == "Classes":
    st.markdown("# Classes")
    st.markdown("## Python Classes")
    st.markdown("Python is an object-oriented programming language. Almost everything in Python is an object, with its properties and methods.")

    st.markdown("## Creating a Class")
    st.markdown("To create a class, use the `class` keyword.")

    st.markdown('''
        ```python
        class MyClass:
            x = 5

        p1 = MyClass()
        print(p1.x) # 5
        ```
        ''')

    st.markdown("## The `__init__()` Function")
    st.markdown("All classes have a function called `__init__()`, which is always executed when the class is being initiated.")

    st.markdown('''
        ```python
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        p1 = Person("John", 36)
        print(p1.name) # John
        print(p1.age) # 36
        ```
        ''')

    st.markdown("## Object Methods")
    st.markdown("Objects can also contain methods. Methods in objects are functions that belong to the object.")

    st.markdown('''
        ```python
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def myfunc(self):
                print("Hello, my name is " + self.name)

        p1 = Person("John", 36)
        p1.myfunc() # Hello, my name is John
        ```
        ''')

    st.markdown("## The `self` Parameter")
    st.markdown("The `self` parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.")

    st.markdown("## Modify Object Properties")
    st.markdown("You can modify properties on objects like this:")

    st.markdown('''
        ```python
        p1.age = 40
        ```
        ''')

    st.markdown("## Delete Object Properties")
    st.markdown("You can delete properties on objects by using the `del` keyword.")

    st.markdown('''
        ```python
        del p1.age
        ```
        ''')

    st.markdown("## Delete Objects")
    st.markdown("You can delete objects by using the `del` keyword.")

    st.markdown('''
        ```python
        del p1
        ```
        ''')

    st.markdown("## Inheritance")
    st.markdown("Inheritance allows us to define a class that inherits all the methods and properties from another class.")

    st.markdown('''
        ```python
        class Student(Person):
            pass

        x = Student("Mike", 22)
        x.myfunc() # Hello, my name is Mike
        ```
        ''')

    st.markdown("## Add Properties")
    st.markdown("You can add properties to the child class.")

    st.markdown('''
        ```python
        class Student(Person):
            def __init__(self, name, age, year):
                super().__init__(name, age)
                self.graduationyear = year

            def welcome(self):
                print("Welcome", self.name, "to the class of", self.graduationyear)

        x = Student("Mike", 22, 2021)
        x.welcome() # Welcome Mike to the class of 2021
        ```
        ''')

    st.markdown("## Good Practices")

    st.markdown("1. Class names should be capitalized, with words separated by underscores as necessary to improve readability.")
    st.markdown("2. Use `__init__()` to initialize the object.")
    st.markdown("3. Use `self` to access the object's properties.")
    st.markdown("4. Use inheritance to reuse code.")
    st.markdown("5. Use `super()` to call the parent class.")
    st.markdown("6. Use docstrings to document the class.")
    st.markdown("7. Use type hints to improve readability.")
    st.markdown("8. Use assertions to check the input.")

    st.markdown("## Example")

    st.markdown('''
        ```python
        class Person:
            def __init__(self, name: str, age: int) -> None:
                """
                This class represents a person.
                name: str: The name of the person.
                age: int: The age of the person.
                """
                assert isinstance(name, str), "name must be a string"
                assert isinstance(age, int), "age must be an integer"
                self.name = name
                self.age = age

            def myfunc(self) -> None:
                """
                This method prints a message.
                """
                print("Hello, my name is " + self.name)

        class Student(Person):
            def __init__(self, name: str, age: int, year: int) -> None:
                super().__init__(name, age)
                self.graduationyear = year

            def welcome(self) -> None:
                """
                This method prints a welcome message.
                """
                print("Welcome", self.name, "to the class of", self.graduationyear)

        p1 = Person("John", 36)
        p1.myfunc() # Hello, my name is John

        x = Student("Mike", 22, 2021)
        x.welcome() # Welcome Mike to the class of 2021
        ```
        ''')

elif subpage == "Modules":
    st.markdown("# Modules")
    st.markdown("## Python Modules")
    st.markdown("A module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py`.")

    st.markdown("## Create a Module")
    st.markdown("To create a module, create a new `.py` file with the module name, and define the functions and variables you want in it.")

    st.markdown("## Use a Module")
    st.markdown("Now we can use the module we just created, by using the `import` statement.")

    st.markdown('''
        ```python
        import mymodule

        print(mymodule.greeting("Jonathan"))
        ```
        ''')

    st.markdown("## Re-naming a Module")
    st.markdown("You can create an alias when you import a module, by using the `as` keyword.")

    st.markdown('''
        ```python
        import mymodule as mx

        print(mx.greeting("Jonathan"))
        ```
        ''')

    st.markdown("## Built-in Modules")
    st.markdown("There are several built-in modules in Python, which you can import whenever you like.")

    st.markdown('''
        ```python
        import platform

        x = platform.system()
        print(x)
        ```
        ''')

    st.markdown("## Using the `dir()` Function")
    st.markdown("There is a built-in function to list all the function names (or variable names) in a module. The `dir()` function.")

    st.markdown('''
        ```python
        import platform

        x = dir(platform)
        print(x)
        ```
        ''')

    st.markdown("## Import From Module")
    st.markdown("You can choose to import only parts from a module, by using the `from` keyword.")

    st.markdown('''
        ```python
        from mymodule import person1

        print(person1["age"])
        ```
        ''')

    st.markdown("## Good Practices")

    st.markdown("1. Module names should be lowercase, with words separated by underscores as necessary to improve readability.")
    st.markdown("2. Use `import` to import modules.")
    st.markdown("3. Use `as` to create an alias for a module.")
    st.markdown("4. Use `dir()` to list all the function names in a module.")
    st.markdown("5. Use `from` to import only parts from a module.")
    st.markdown("6. Use docstrings to document the module.")
    st.markdown("7. Use type hints to improve readability.")
    st.markdown("8. Use assertions to check the input.")

    st.markdown("## Example")

    st.markdown('''
        ```python
        import mymodule

        print(mymodule.greeting("Jonathan"))

        import mymodule as mx

        print(mx.greeting("Jonathan"))

        import platform

        x = platform.system()
        print(x)

        import platform

        x = dir(platform)
        print(x)

        from mymodule import person1

        print(person1["age"])
        ```
        ''')

elif subpage == "Packages":
    st.markdown("# Packages")
    st.markdown("## Python Packages")
    st.markdown("A package is a collection of modules. It must have a special file called `__init__.py`, which can be empty.")

    st.markdown("## Create a Package")
    st.markdown("To create a package, create a new directory with the package name, and add a file named `__init__.py`.")

    st.markdown("## Use a Package")
    st.markdown("Now we can use the package we just created, by using the `import` statement.")

    st.markdown('''
        ```python
        import mypackage.mymodule

        a = mypackage.mymodule.person1["age"]
        print(a)
        ```
        ''')

    st.markdown("## Re-naming a Package")
    st.markdown("You can create an alias when you import a package, by using the `as` keyword.")

    st.markdown('''
        ```python
        import mypackage.mymodule as mx

        a = mx.person1["age"]

        print(a)
        ```
        ''')

    st.markdown("## Good Practices")

    st.markdown("1. Package names should be lowercase, with words separated by underscores as necessary to improve readability.")
    st.markdown("2. Use `import` to import packages.")
    st.markdown("3. Use `as` to create an alias for a package.")
    st.markdown("4. Use docstrings to document the package.")
    st.markdown("5. Use type hints to improve readability.")
    st.markdown("6. Use assertions to check the input.")

    st.markdown("## Example")

    st.markdown('''
        ```python
        import mypackage.mymodule

        a = mypackage.mymodule.person1["age"]
        print(a)

        import mypackage.mymodule as mx

        a = mx.person1["age"]

        print(a)
        ```
        ''')

elif subpage == "File I/O":
    st.markdown("# File Handling")
    st.markdown("## Python File Handling")
    st.markdown("Python can read and write files, which are handled using file objects. Files are opened in read (`r`), write (`w`), or append (`a`) mode.")

    st.markdown("## Open a File")
    st.markdown("To open a file, use the built-in `open()` function, with one of the following parameters:")

    st.markdown("1. `r` - Read - Default value. Opens a file for reading, error if the file does not exist.")
    st.markdown("2. `a` - Append - Opens a file for appending, creates the file if it does not exist.")
    st.markdown("3. `w` - Write - Opens a file for writing, creates the file if it does not exist.")
    st.markdown("4. `x` - Create - Creates the specified file, returns an error if the file exists.")

    st.markdown("## Read a File")
    st.markdown("To read a file, use the `read()` method.")

    st.markdown('''
        ```python
        f = open("demofile.txt", "r")
        print(f.read())
        ```
        ''')

    st.markdown("## Read Only Parts of the File")
    st.markdown("By default the `read()` method returns the whole text, but you can also specify how many characters you want to return.")

    st.markdown('''
        ```python
        f = open("demofile.txt", "r")
        print(f.read(5))
        ```
        ''')

    st.markdown("## Read Lines")
    st.markdown("You can return one line by using the `readline()` method.")

    st.markdown('''
        ```python
        f = open("demofile.txt", "r")
        print(f.readline())
        ```
        ''')

    st.markdown("By calling `readline()` two times, you can read the two first lines.")

    st.markdown('''
        ```python
        f = open("demofile.txt", "r")
        print(f.readline())
        print(f.readline())
        ```
        ''')

    st.markdown("By looping through the lines of the file, you can read the whole file, line by line.")

    st.markdown('''
        ```python
        f = open("demofile.txt", "r")
        for x in f:
            print(x)

        f.close()
        ```
        ''')

    st.markdown("## Close Files")
    st.markdown("It is a good practice to always close the file when you are done with it.")

    st.markdown('''
        ```python
        f = open("demofile.txt", "r")
        print(f.readline())
        f.close()
        ```
        ''')

    st.markdown("## Write to an Existing File")
    st.markdown("To write to an existing file, you must add a parameter to the `open()` function:")

    st.markdown("1. `a` - Append - will append to the end of the file.")
    st.markdown("2. `w` - Write - will overwrite any existing content.")

    st.markdown('''
        ```python
        f = open("demofile.txt", "a")
        f.write("Now the file has more content!")
        f.close()

        f = open("demofile.txt", "r")
        print(f.read())
        f.close()
        ```
        ''')

    st.markdown("## Create a New File")
    st.markdown("To create a new file in Python, use the `open()` method, with one of the following parameters:")

    st.markdown("1. `x` - Create - will create a file, returns an error if the file exist.")
    st.markdown("2. `w` - Write - will create a file if the specified file does not exist.")

    st.markdown('''
        ```python
        f = open("myfile.txt", "x")
        f.close()
        ```
        ''')

    st.markdown("## Delete a File")
    st.markdown("To delete a file, you must import the OS module, and run its `os.remove()` function.")

    st.markdown('''
        ```python
        import os
        os.remove("demofile.txt")
        ```
        ''')

    st.markdown("## Check if File Exists")
    st.markdown("To avoid getting an error, you might want to check if the file exists before you try to delete it.")

    st.markdown('''
        ```python
        import os
        if os.path.exists("demofile.txt"):
            os.remove("demofile.txt")
        else:
            print("The file does not exist")

        f = open("demofile.txt", "x")
        f.close()
        ```
        ''')

    st.markdown("## Delete Folder")
    st.markdown("To delete an entire folder, use the `os.rmdir()` method.")

    st.markdown('''
        ```python
        import os
        os.rmdir("myfolder")
        ```
        ''')
