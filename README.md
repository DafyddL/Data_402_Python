![](https://www.python.org/static/img/python-logo.png)
# Python Fundamentals
This is a written guide based on the SpartaGlobal Academy Python Fundamentals course.

## Data Types
There are three primary types of data we will be looking at:
- [Numbers](#Numbers-and-Maths-Operators)
  - Integers (whole numbers) i.e. 1, 128
  - Floating point numbers (decimal numbers) i.e. 5.47, 97.452
- [Strings](#Strings)
  - "Anything with characters or text involved"
- [Boolean](#Booleans-and-Equality-Operators)
  - <span style="color:green">True</span> or <span style="color:red">False</span>

We can find the type of a variable using `type()` function. For example:
```python
>>> type(3)
<class 'int'>

>>> type("Hello World")
<class 'str'>

>>> type(False)
<class 'bool'>
```
### Numbers and Maths Operators
We have previously defined our two types of number:
  - Integers (whole numbers) i.e. 1, 128
  - Floating point numbers (decimal numbers) i.e. 5.47, 97.452

Next we will look at the 5 different standard operators:
- Addition `+` is the standard maths function of adding one number to another
e.g. 
    ```python
    >>> print(5+5.5)
  10.5
    ```
- Subtraction `-` is the standard maths function of subtracting one number from another e.g.
    ```python
    >>>print(5-5.5)
    -0.5
    ```
- Multiplication `*` is the standard maths function of multiplying one number by another e.g.
    ```python
    >>> print(5*8)
    40
    ```
- Division `/` is the standard maths function of dividing one number by another e.g.
    ```python
    >>> print(5/8)
    0.625
    ```
- Modulo `%` is possibly a new function to you. It takes the first number, calculates how many times the second number fits into the first, and returns the remainder e.g.  
   If I had 17 apples, and wanted to split them evenly between 3 people, I would give each person 5 apples and have **2 remaining apples** so
    ```python
    >>> print(17%3)
    2
    ```

### Strings
Strings are anything containing characters or text. We can define string using either single quotations like `'Hello World'` or double quotations like `"Hello World"`.  
It is important to know that python (like other programming languages) does not see words/characters in the same way as you and I. Python instead reads them as a list of unicode characters. e.g.  
We can print the character `a` using either
```python
>>> print('a')
a
  ```
or we can print by explicitly giving the unicode of the character
```python
>>> print(u'\u0061')
a
```

Since python interprets stings as simply a list of unicode characters, we can reference locations in the string. e.g.  
```python
>>> print("Hello World"[3])
l
```
*N.B. Python (like many programming languages) starts indexing at 0. So the first character in this string is referenced using `[0]`, second using `[1]`, and so on...*

We can also reference backwards, so if we wanted to find the last character of the string we could use:  
```python
>>> print("Hello World"[-1])
d'
```

*N.B. **Careful** If we try to reference outside the bounds of the string like 15th character of a 10 letter string, we will receive an error `IndexError: string index out of range`*

We can use the function `len()` do find the length of an object in python, like a string e.g.
```python
>>> print(len("Hello World"))
11
```
This can help us make sure we do not index outside the bounds of the object.
#### Concatenation
With strings, we can concatenate them together
```python
>>> "Hello" + " " + "World"
'Hello World'
```
We do need to specify every character for the concatenation i.e. python will not insert spaces unless we specify a space.

We can also convert other data types to strings using the str() function. e.g.
```python
>>> "My age is " + str(42)
'My age is 42'
```
#### Escape characters
THere are some characters which we may want to include in a string, but python considers them special.
One prime example of this `"`.
We can use a `\` to escape to specify to python to interpret this as a character, not as the special meaning python interprets them as.
e.g.
```python
>>> "This is a "quotation""
ERROR
```
```python
>>> "This is a \"quotation\""
'This is a "quotation"'
```

#### String Methods

We have many string methods:
- `"my string".capitalize()` - Capitalises the first letter `"My string"`
- `"my string".upper()` - capitalises every letter `"MY STRING"`
- `"my string".lower()` - similar to above
- `"my string".replace('i',' ')` - replaces all instances of the first specified string with the second `"my str ng"`

### Booleans and Equality Operators
Finally we have booleans, that is either <span style="color:green">True</span> or <span style="color:red">False</span>.

We can perform equality operators.
These operators compare two types of data and return a boolean on the outcome of the operator.
There are six equality operators:  
|Operator  | Meaning |Example|
--------  |-------- |-------
`==`      | equal to | 4 == 4 (<span style="color:green">True</span>)

## Variables

We can store our data in variables. 
Variables are not of static type, so we can change the type of the variable. 
e.g.
```python
>>> a = 4
>>> print(a)
4

>>> a = "Hello World"
>>> print(a)
Hello World
```

## Control Flow Variables

Control flow variables are used to control the flow of the python code.
The most common method is using if-else statements e.g.
```python
if condition1
    do stuff
elif condition2:
    do other stuff
elif condition3:
    do other other stuff
else:
    do something else
```
Here we check an [equality statement](#Booleans-and-Equality-Operators) condition1, and if it is true it runs the `do stuff code`.
If condition1 is False, we check condition2.
If condition2 is True, we `do other stuff`.
If condition2 is False, we check condition3.
etc.
If all conditions are false, the code follows `else` and does something else

## Collections

### Lists
A list is exactly that. 
A list of variables.
All variables must be the same type and can be indexed in order with 0 being the first item.
We can declare a list using
```python
my_list = ["this", "is", "my","list","of","strings"]

>>> my_list[2]
'my'
```


### Dictionaries

Dictionaries are a collection of items. 
They do not have to be all of the same data type.
They use pairs of variables called keys and values.
The values are what we're storing and the key is the method of referencing said variable. e.g.
```python
>>>my_dict = {"First Name": "John",
            "Last Name": "Smith",
            "Age": 42}
>>> my_dict["Last Name"]
'Smith'
```

## Loops

### While Loops
```python
while (equality operator):
    do stuff
```

Here , the code `do stuff` will be run in a loop until the equality operator is no longer True
### For Loops
```python
for i in my_list:
  do stuff 
```

Similar to the while loop, the for loop runs the `do stuff` code as many times as there are items in `my_list`.
We can also use `i` to reference each item in `my_list`. 
Say we ran a for loop on a list of 5 items, `i` would represent the item in the list with index the same as how many times the loop has run.

## Functions
```python
def my_function(input1, input2, ...):
    Body of function (do stuff with the inputs)
    
    return output1, output2, ...
```
Here, the function is defined with input variables.
The body describes all the code we wish to run using those input variables.
It then returns any output variable we wish - this closes the function.


We can apply this function at any time, run it as many times we like, with any change to the input variables we like.
