## What is API?
(Application Programming Interface) API is a set of programming interfaces that enables you to build applications that run on different platforms.

Simply
- **Interface** between **two** systems
- Provides a way to **access data** from one system to another
- Allows you to build applications that run on **different platforms**

## What is JSON?
(Javascript Object Notation) JSON
Basically it's **similar** to a **javascript object**, but it's main purpose is to be used in web applications for *transferring data.*

## What is HTTP?
(Hypertext Transfer Protocol) HTTP is a **standard** for **transferring data** between **two** systems.

Basically it's a way for clients to **communicate** with servers.


## What is REST?
(Representational State Transfer) REST is a set of architectural principles for building web services.

Simply
- **Software architecture style** that defines a set of rules for **web services**
- Uniform Interface
- Stateless
- Cacheable
- Client-Server


## GET
- **Get** is a **method** that **retrieves** data from a **server**.

e.g. | `GET /users/1` | `GET google.com/search?q=hello` | 

## POST
- **Post** is a **method** that **adds** data to a **server**.

e.g. | `POST /users` with `{ "name": "John" }`

## PUT
- **Put** is a **method** that **updates** data on a **server**.

e.g. | `PUT /users/1` with `{ "name": "John" }`

## DELETE
- **Delete** is a **method** that **deletes** data from a **server**.

e.g. | `DELETE /users/1` |


## How to use API?
Usually, when ever we visit a website, we get a **response** from the server. This response is usually in **JSON** format. 

So, unknowningly we are using API to access data from the server.
Whether it is to get instagram posts, or to post on instagram, we are using API, to access and write data on a server.

To use API, we don't usually need any special tools, we just need to know how to use HTTP methods. i.e. we can work on it in the browser. But I was thinking that we can try to use some tools today instead, to access these APIs.

## How to get data from API?
To get data from API, we need to use **GET** method. Or simply we can type the URL in the browser.

## How to send data to API?
To send data to API, we need to use **POST** method. It's the same thing used by forms in HTML, where we specify the data that we want to send. and we send it to the server. using the action attribute as URI.

## What is FLASK?
(Flask) Flask is a microframework for Python.
i.e. it's a small framework that allows you to build web applications using Python. It's very **easy to write**, and it's **very fast**. being a microframework, it's **easy to scale**.

## What is FastAPI?
(FastAPI) FastAPI is a microframework for Python.
It consists of a set of **simple and powerful tools**, that make it **easy to write**, and **fast**.
Special features of FastAPI:
- **Stateless**
- **Cacheable**
- **Uniform Interface**
- **Simple**
- **Fast**
- **Lightweight**
- **Simple to use**
- **Easy to learn**
- Works with pydantic, marshmallow, starlette and more.


## Postman
[Postman](https://www.getpostman.com/docs/), is a tool that allows you to **test** your API.
Features include:
- **Visual**
- **Code**
- **Run**
- **Debug**
- **Export**
- etc.

## Python.requests
[Python.requests](https://requests.readthedocs.io/en/master/), is a library that allows you to **send** requests to **servers**.
Features include:
- **GET**
- **POST**
- **PUT**
- **DELETE**
- Other features include **headers**, **cookies**, **params**, **files**, **auth**, **timeout**, **proxies**, **verify**, **cert**, **json**, **stream**, etc.

## References
<!-- References mentioned from above -->
- [API](https://en.wikipedia.org/wiki/Application_programming_interface)
- [JSON](https://en.wikipedia.org/wiki/JSON)
- [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
- [REST](https://en.wikipedia.org/wiki/Representational_state_transfer)
- [Flask](https://www.getflask.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Postman](https://www.getpostman.com/)
- [Python.requests](https://requests.readthedocs.io/)
