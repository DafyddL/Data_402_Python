# JSON and APIs

## JSON

### What does it stand for?
JSON stands for JavaScript Object Notation. 

### What is it used for?

It is used in object-oriented programming that uses human-readable language, text, and syntax to store and communicate data objects between applications.
In other terms, it is a file for storing objects.
The file format is understood by many different languages, so can be useful for transferring objects between languages.
It is also designed to be human-readable, so if a person were to open the file in a text editor, the structure and data would be easily understood.


### What is it written in?

JSON is written in a subset of the JavaScript scripting language - language that JSON files are commonly used in.
Despite this, code for parsing and generating JSON data is readily available in many programming languages.

### What is the JSON syntax for:
#### Name-Value pairs:
A name/value pair consists of a field name (in double quotes), followed by a colon, followed by a value:
```json
"firstName":"John"
```
#### Objects
Similar to a dictionary in python, objects contain multiple name/value pairs
```json
{"firstName":"John", "lastName":"Smith"}
```

#### Separating Objects
Objects in JSON are enclosed in squiggly brackets as above, and separated simply with a comma
```json
{"firstName":"John","lastName":"Smith"},{"firstname":"Anna","lastName":"Jones"}
```

#### JSON arrays
A JSON array looks similar to a python list of dictionaries
```json
"employees":[
{"firstName":"John","lastName":"Smith"},
{"firstname":"Anna","lastName":"Jones"},
{"firstName":"Angus","lastName":"McCoy"}
]
```