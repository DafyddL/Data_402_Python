# JSON and APIs

## JSON

### What does it stand for?
JSON stands for JavaScript Object Notation. 

### What data types can it store/uses?
 - Strings
 - Numbers
 - Lists
 - Booleans
 - Nulls
 - Objects (dictionaries)

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

## APIs

### What are APIs?
An Application Program Interface (API) is a mechanism that enables two software components to communicate with each other using a set of definitions and protocols.
It's like two people who speak different languages speaking with a phrase book. 
You both may not be able to understand each9other directly, but the phrasebooks give you phrases (definitions) that the other will be able to answer.

### How are APIs used and why are they popular
APIs are typically used in terms of a client and a server. 
One application (client) sends a request to the other client (server) and the other client (server) responds.
For example, if the client wanted weather data, it could request the data from a weather service server with an API.

APIs are popular as they allow different applications to communicate in **real time**. Also applications of different origins can communicate with each other.
One example of this would be for weather (as above).
There is no need for the client application to collect/generate the weather data itself, it can simply request that data from another application.
### Find a diagram that showcases the API data TRANSFER PROCESS.
![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*5_VEtMBQg9h-WossdhK3Ow.png)

### What is a REST API?
A REpresentational State Transfer (REST) API that conform to the REST architectural constraints and allows for interaction with the RESTful web services.
Essentially, an API is a REST api if it conforms to the criteria:
- A client-server architecture made of clients, servers, and resources. Requests are managed through http.
- Stateless client-server communication - no client information is stored between get requests and each request is separate and unconnected.
- Cacheable data that streamlines client-server interactions
- A uniform interface between components so that information is transferred in a standard form. This requires that:
  - resources are requested are identifiable and separate from the representations sent to the client
  - resources can be manipulated by the client via a representation they recevie because the representation contains enough information to do so - **you shouldn't need to make a second request because there was not enough information in the first**.
  - self-descriptive messages returned to thwe client have enough information to describe how the client should process - **If a message is sent to the client, it should not be vague**
  - hypertext/hypermedia is available- **after accessing the resource, there should be hyperlinks to find all other currently available actions**.
-A layered system that organizes each type of server involved in the retrieval of requested information into hierarchies, invisible to the client
So an API is RESTful if it is Representational, has URIs , is , and has Caching
### What is HTTP?
HyperText Transfer Protocol (HTTP) is an application layer protocol used to transfer information between networked devices.

### Find diagrams that showcase:
#### HTTP Request Structure
![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*i2tUjWy44-dYT9qsaWbvig.png)
#### HTTP Response Structure
![](https://miro.medium.com/v2/resize:fit:720/format:webp/1*w4gDd2TFunoOnrWy3xpHkQ.png)

### What are the 5 http verbs?
| HTTP Verb | Description                             | CRUD           | Entire Collection (e.g. /customers)                                                                  | Specific Item (e.g. /customers/{id})                                                   |
|-----------|-----------------------------------------|----------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| POST      | Create new resources                    | Create         | 201 (Created), 'Location' header with link to /customers/{id} containing new ID.                     | 	404 (Not Found), 409 (Conflict) if resource already exists..                          |
| GET       | Retrieve a representation of a resource | Read           | 	200 (OK), list of customers. Use pagination, sorting and filtering to navigate big lists.           | 200 (OK), single customer. 404 (Not Found), if ID not found or invalid.                |
| PUT       | Create/Update a resource                | Update/Replace | 405 (Method Not Allowed), unless you want to update/replace every resource in the entire collection. | collection.	200 (OK) or 204 (No Content). 404 (Not Found), if ID not found or invalid. |
| PATCH     | Updates part of a resource              | Update/Modify  | 405 (Method Not Allowed), unless you want to modify the collection itself.                           | 200 (OK) or 204 (No Content). 404 (Not Found), if ID not found or invalid.             |
| DELETE    | Delete a resource                       | Delete         | 	405 (Method Not Allowed), unless you want to delete the whole collection—not often desirable.       | 200 (OK). 404 (Not Found), if ID not found or invalid.                                 |