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
d
```

*N.B. **Careful** If we try to reference outside the bounds of the string like 15th character of a 10 letter string, we will receive an error `IndexError: string index out of range`*

We can use the function `len()` do find the length of an object in python, like a string e.g.
```python
>>> print(len("Hello World"))
11
```
This can help us make sure we do not index outside the bounds of the object

### Booleans and Equality Operators
Finally we have booleans, that is either <span style="color:green">True</span> or <span style="color:red">False</span>.

We can 