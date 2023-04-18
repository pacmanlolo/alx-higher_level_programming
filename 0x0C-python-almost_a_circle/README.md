1. Base class
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write the first class Base:

Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

Create a file named models/base.py:

Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
otherwise, increment __nb_objects and assign the new value to the public instance attribute id
This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

2. First Rectangle
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write the class Rectangle that inherits from Base:

In the file models/rectangle.py
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter:
__width -> width
__height -> height
__x -> x
__y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Call the super class with id - this super call with use the logic of the __init__ of the Base class
Assign each argument width, height, x and y to the right attribute
Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.

3. Validate attributes
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):

If the input is not an integer, raise the TypeError exception with the message: <name of the attribute> must be an integer. Example: width must be an integer
If width or height is under or equals 0, raise the ValueError exception with the message: <name of the attribute> must be > 0. Example: width must be > 0
If x or y is under 0, raise the ValueError exception with the message: <name of the attribute> must be >= 0. Example: x must be >= 0

4. Area first
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.


5. Display #0
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.


6. __str__
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>


7. Display #1
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y


8. Update #0
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:

1st argument should be the id attribute
2nd argument should be the width attribute
3rd argument should be the height attribute
4th argument should be the x attribute
5th argument should be the y attribute
This type of argument is called a “no-keyword argument” - Argument order is super important.


9. Update #1
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:

**kwargs can be thought of as a double pointer to a dictionary: key/value
As Python doesn’t have pointers, **kwargs is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
**kwargs must be skipped if *args exists and is not empty
Each key in this dictionary represents an attribute to the instance
This type of argument is called a “key-worded argument”. Argument order is not important.


10. And now, the Square!
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write the class Square that inherits from Rectangle:

In the file models/square.py
Class Square inherits from Rectangle
Class constructor: def __init__(self, size, x=0, y=0, id=None)::
Call the super class with id, x, y, width and height - this super call will use the logic of the __init__ of the Rectangle class. The width and height must be assigned to the value of size
You must not create new attributes for this class, use all attributes of Rectangle - As reminder: a Square is a Rectangle with the same width and height
All width, height, x and y validation must inherit from Rectangle - same behavior in case of wrong data
The overloading __str__ method should return [Square] (<id>) <x>/<y> - <size> - in our case, width or height
As you know, a Square is a special Rectangle, so it makes sense this class Square inherits from Rectangle. Now you have a Square class who has the same attributes and same methods.


11. Square size
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Square by adding the public getter and setter size

The setter should assign (in this order) the width and the height - with the same value
The setter should have the same value validation as the Rectangle for width and height - No need to change the exception error message (It should be the one from width)


12. Square update
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:

*args is the list of arguments - no-keyworded arguments
1st argument should be the id attribute
2nd argument should be the size attribute
3rd argument should be the x attribute
4th argument should be the y attribute
**kwargs can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
**kwargs must be skipped if *args exists and is not empty
Each key in this dictionary represents an attribute to the instance


13. Rectangle instance to dictionary representation
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle:

This dictionary must contain:

id
width
height
x
y


14. Square instance to dictionary representation
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square:

This dictionary must contain:

id
size
x
y


15. Dictionary to JSON string
mandatory
Score: 0.0% (Checks completed: 0.0%)
JSON is one of the standard formats for sharing data representation.

Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries:

list_dictionaries is a list of dictionaries
If list_dictionaries is None or empty, return the string: "[]"
Otherwise, return the JSON string representation of list_dictionaries


16. JSON string to file
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:

list_objs is a list of instances who inherits of Base - example: list of Rectangle or list of Square instances
If list_objs is None, save an empty list
The filename must be: <Class name>.json - example: Rectangle.json
You must use the static method to_json_string (created before)
You must overwrite the file if it already exists


17. JSON string to dictionary
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string:

json_string is a string representing a list of dictionaries
If json_string is None or empty, return an empty list
Otherwise, return the list represented by json_string


root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# cd ..
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle# cd tests/
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/tests# cd test_models/
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/tests/test_models# git add .
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/tests/test_models# git commit -m "another 1"
[main 3806a59] another 1
 9 files changed, 2006 insertions(+)
 mode change 100644 => 100755 0x0C-python-almost_a_circle/tests/test_models/__init__.py
 create mode 100644 0x0C-python-almost_a_circle/tests/test_models/__pycache__/__init__.cpython-38.pyc
 create mode 100644 0x0C-python-almost_a_circle/tests/test_models/__pycache__/test_base.cpython-38.pyc
 create mode 100644 0x0C-python-almost_a_circle/tests/test_models/__pycache__/test_rectangle.cpython-38.pyc
 create mode 100644 0x0C-python-almost_a_circle/tests/test_models/__pycache__/test_square.cpython-38.pyc
 create mode 100755 0x0C-python-almost_a_circle/tests/test_models/test_base.py
 mode change 100644 => 100755 0x0C-python-almost_a_circle/tests/test_models/test_rectangle.py
 mode change 100644 => 100755 0x0C-python-almost_a_circle/tests/test_models/test_square.py
 delete mode 100644 "0x0C-python-almost_a_circle/tests/test_models/\302\226test_base.py"
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/tests/test_models# git push
Password for 'https://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@github.com':
Enumerating objects: 19, done.
Counting objects: 100% (18/18), done.
Delta compression using up to 2 threads
Compressing objects: 100% (12/12), done.
Writing objects: 100% (13/13), 28.11 KiB | 279.00 KiB/s, done.
Total 13 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 1 local object.
To https://github.com/pacmanlolo/alx-higher_level_programming.git
   364b5d6..3806a59  main -> main
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/tests/test_models# cd ..
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/tests# cd ..
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle# ls
models  tests
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle# cd models/
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# ls
base.py  __init__.py  __pycache__  rectangle.py  square.py
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# chmod u+x *.py
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# ls
base.py  __init__.py  __pycache__  rectangle.py  square.py
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# git add .        root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# git commit -m "another 1"
[main 2e18048] another 1
 8 files changed, 1 insertion(+), 1 deletion(-)
 mode change 100644 => 100755 0x0C-python-almost_a_circle/models/__init__.py
 create mode 100644 0x0C-python-almost_a_circle/models/__pycache__/__init__.cpython-38.pyc
 create mode 100644 0x0C-python-almost_a_circle/models/__pycache__/base.cpython-38.pyc
 create mode 100644 0x0C-python-almost_a_circle/models/__pycache__/rectangle.cpython-38.pyc
 create mode 100644 0x0C-python-almost_a_circle/models/__pycache__/square.cpython-38.pyc
 mode change 100644 => 100755 0x0C-python-almost_a_circle/models/base.py
 mode change 100644 => 100755 0x0C-python-almost_a_circle/models/rectangle.py
 mode change 100644 => 100755 0x0C-python-almost_a_circle/models/square.py
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# git push
Password for 'https://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@github.com':
Enumerating objects: 14, done.
Counting objects: 100% (14/14), done.
Delta compression using up to 2 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (10/10), 5.93 KiB | 2.96 MiB/s, done.
Total 10 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/pacmanlolo/alx-higher_level_programming.git
   3806a59..2e18048  main -> main
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# ls
base.py  __init__.py  __pycache__  rectangle.py  square.py
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# vi base.py
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# vi __init__.py
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# vi rectangle.py
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# vi square.py
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# pycodestyle base.py
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# pycodestyle rectangle.py
rectangle.py:139:1: E265 block comment should start with '# '
rectangle.py:141:1: E402 module level import not at top of file
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# vi rectangle.py
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# pycodestyle rectangle.py
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# pycodestyle square.py
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# git add .
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# git commit -m "correction"
[main ba325b9] correction
 2 files changed, 1 insertion(+), 8 deletions(-)
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# git push
Password for 'https://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@github.com':
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 2 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 495 bytes | 495.00 KiB/s, done.
Total 6 (delta 4), reused 0 (delta 0)
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
To https://github.com/pacmanlolo/alx-higher_level_programming.git
   2e18048..ba325b9  main -> main
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle/models# cd ..
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle# python3 -m unittest discover tests
....................................................................................................................................................................................................................................................................................................................................................................................
----------------------------------------------------------------------
Ran 372 tests in 0.404s

OK
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle# git add .
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle# git commit -m "correction"
[main 5e6cd48] correction
 4 files changed, 0 insertions(+), 0 deletions(-)
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle# git push
Password for 'https://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@github.com':
Enumerating objects: 14, done.
Counting objects: 100% (14/14), done.
Delta compression using up to 2 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (9/9), 5.65 KiB | 642.00 KiB/s, done.
Total 9 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/pacmanlolo/alx-higher_level_programming.git
   ba325b9..5e6cd48  main -> main
root@19c3b4e13647:/alx-higher_level_programming/0x0C-python-almost_a_circle# cat > README.md
1. Base class
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write the first class Base:

Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

Create a file named models/base.py:

Class Base:
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
otherwise, increment __nb_objects and assign the new value to the public instance attribute id
This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

2. First Rectangle
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write the class Rectangle that inherits from Base:

In the file models/rectangle.py
Class Rectangle inherits from Base
Private instance attributes, each with its own public getter and setter:
__width -> width
__height -> height
__x -> x
__y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Call the super class with id - this super call with use the logic of the __init__ of the Base class
Assign each argument width, height, x and y to the right attribute
Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.

3. Validate attributes
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):

If the input is not an integer, raise the TypeError exception with the message: <name of the attribute> must be an integer. Example: width must be an integer
If width or height is under or equals 0, raise the ValueError exception with the message: <name of the attribute> must be > 0. Example: width must be > 0
If x or y is under 0, raise the ValueError exception with the message: <name of the attribute> must be >= 0. Example: x must be >= 0

4. Area first
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.


5. Display #0
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.


6. __str__
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>


7. Display #1
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y


8. Update #0
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:

1st argument should be the id attribute
2nd argument should be the width attribute
3rd argument should be the height attribute
4th argument should be the x attribute
5th argument should be the y attribute
This type of argument is called a “no-keyword argument” - Argument order is super important.


9. Update #1
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:

**kwargs can be thought of as a double pointer to a dictionary: key/value
As Python doesn’t have pointers, **kwargs is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
**kwargs must be skipped if *args exists and is not empty
Each key in this dictionary represents an attribute to the instance
This type of argument is called a “key-worded argument”. Argument order is not important.


10. And now, the Square!
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write the class Square that inherits from Rectangle:

In the file models/square.py
Class Square inherits from Rectangle
Class constructor: def __init__(self, size, x=0, y=0, id=None)::
Call the super class with id, x, y, width and height - this super call will use the logic of the __init__ of the Rectangle class. The width and height must be assigned to the value of size
You must not create new attributes for this class, use all attributes of Rectangle - As reminder: a Square is a Rectangle with the same width and height
All width, height, x and y validation must inherit from Rectangle - same behavior in case of wrong data
The overloading __str__ method should return [Square] (<id>) <x>/<y> - <size> - in our case, width or height
As you know, a Square is a special Rectangle, so it makes sense this class Square inherits from Rectangle. Now you have a Square class who has the same attributes and same methods.


11. Square size
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Square by adding the public getter and setter size

The setter should assign (in this order) the width and the height - with the same value
The setter should have the same value validation as the Rectangle for width and height - No need to change the exception error message (It should be the one from width)


12. Square update
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:

*args is the list of arguments - no-keyworded arguments
1st argument should be the id attribute
2nd argument should be the size attribute
3rd argument should be the x attribute
4th argument should be the y attribute
**kwargs can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
**kwargs must be skipped if *args exists and is not empty
Each key in this dictionary represents an attribute to the instance


13. Rectangle instance to dictionary representation
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle:

This dictionary must contain:

id
width
height
x
y


14. Square instance to dictionary representation
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square:

This dictionary must contain:

id
size
x
y


15. Dictionary to JSON string
mandatory
Score: 0.0% (Checks completed: 0.0%)
JSON is one of the standard formats for sharing data representation.

Update the class Base by adding the static method def to_json_string(list_dictionaries): that returns the JSON string representation of list_dictionaries:

list_dictionaries is a list of dictionaries
If list_dictionaries is None or empty, return the string: "[]"
Otherwise, return the JSON string representation of list_dictionaries


16. JSON string to file
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:

list_objs is a list of instances who inherits of Base - example: list of Rectangle or list of Square instances
If list_objs is None, save an empty list
The filename must be: <Class name>.json - example: Rectangle.json
You must use the static method to_json_string (created before)
You must overwrite the file if it already exists


17. JSON string to dictionary
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string:

json_string is a string representing a list of dictionaries
If json_string is None or empty, return an empty list
Otherwise, return the list represented by json_string

18. Dictionary to Instance
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set:

**dictionary can be thought of as a double pointer to a dictionary
To use the update method to assign all attributes, you must create a “dummy” instance before:
Create a Rectangle or Square instance with “dummy” mandatory attributes (width, height, size, etc.)
Call update instance method to this “dummy” instance to apply your real values
You must use the method def update(self, *args, **kwargs)
**dictionary must be used as **kwargs of the method update
You are not allowed to use eval


19. File to instances
mandatory
Score: 0.0% (Checks completed: 0.0%)
Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:

The filename must be: <Class name>.json - example: Rectangle.json
If the file doesn’t exist, return an empty list
Otherwise, return a list of instances - the type of these instances depends on cls (current class using this method)
You must use the from_json_string and create methods (implemented previously)


20. JSON ok, but CSV?
#advanced
Score: 0.0% (Checks completed: 0.0%)
Update the class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls): that serializes and deserializes in CSV:

The filename must be: <Class name>.csv - example: Rectangle.csv
Has the same behavior as the JSON serialization/deserialization
Format of the CSV:
Rectangle: <id>,<width>,<height>,<x>,<y>
Square: <id>,<size>,<x>,<y>


21. Let's draw it
#advanced
Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares:

You must use the Turtle graphics module
To install it: sudo apt-get install python3-tk
To make the GUI available outside your vagrant machine, add this line in your Vagrantfile: config.ssh.forward_x11 = true
No constraints for color, shape etc… be creative!