# controllers.mainControllers

## generate_token
```python
generate_token(user)
```
Generates a JWT-like auth token

Arguments:
    user {User} -- A SequelAlchemy user object

Returns:
    str -- The token

## read_token
```python
read_token(token)
```
Validates the token payload with the signature, and returns
a dict containing the user data in the payload

Arguments:
    token {str} -- The token passed in the HTTP header

Returns:
    dict -- The decoded user data

## this_user
```python
this_user()
```
Gets the current user's info from token

Returns:
    dict -- The user's data

## authenticate
```python
authenticate(func)
```
A decorator method that checks that the user's auth token is valid

Arguments:
    func {func} -- The target method

Returns:
    func -- The target method

## OrganizationList
```python
OrganizationList(self, /, *args, **kwargs)
```

### methods
set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.
### get
```python
OrganizationList.get(self)
```
Handles GET requests for /orgs endpoint

Returns:
    list -- Returns list of organizations

### post
```python
OrganizationList.post(self)
```
Handles POST requests for /orgs endpoint

Returns:
    dict -- Status message

## OrganizationController
```python
OrganizationController(self, /, *args, **kwargs)
```

### methods
set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.
## NewsController
```python
NewsController(self, /, *args, **kwargs)
```

### methods
set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.
### get
```python
NewsController.get(self, news_keyword)
```
Handles GET requests for /news/<news_keyword> endpoint

Arguments:
    news_keyword {str} -- The query to search for

Returns:
    list -- A list of news items

# controllers.userController

## LoginController
```python
LoginController(self, /, *args, **kwargs)
```

### methods
set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.
### post
```python
LoginController.post(self)
```
The POST handler for the /login endpoint

Returns:
    dict -- Object containing the token and user details

## CreateAccountController
```python
CreateAccountController(self, /, *args, **kwargs)
```

### methods
set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.
### post
```python
CreateAccountController.post(self)
```
The POST handler for the /create_account endpoint

Returns:
    dict -- Status message

## UserList
```python
UserList(self, /, *args, **kwargs)
```

### method_decorators
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
### methods
set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.
### get
```python
UserList.get(self)
```
The GET hanlder for the /users endpoint

Returns:
    list -- List of users

## UserController
```python
UserController(self, /, *args, **kwargs)
```

### method_decorators
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
### methods
set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.
### get
```python
UserController.get(self, user_id)
```
The GET handler for the /users/<user_id> endpoint

Arguments:
    user_id {int} -- The user's id

Returns:
    dict -- Data about the user

### put
```python
UserController.put(self, user_id)
```
The PUT handler for the /users/<user_id> endpoint

Arguments:
    user_id {int} -- The user's id

Returns:
    dict -- Data about the modified user

### delete
```python
UserController.delete(self, user_id)
```
The DELETE handler for the /users/<user_id> endpoint

Arguments:
    user_id {int} -- The user's id

Returns:
    dict -- Status message

