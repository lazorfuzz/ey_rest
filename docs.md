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

## OrganizationController
```python
OrganizationController(self, /, *args, **kwargs)
```

## NewsController
```python
NewsController(self, /, *args, **kwargs)
```

# controllers.userController

## LoginController
```python
LoginController(self, /, *args, **kwargs)
```

## CreateAccountController
```python
CreateAccountController(self, /, *args, **kwargs)
```

## UserList
```python
UserList(self, /, *args, **kwargs)
```

## UserController
```python
UserController(self, /, *args, **kwargs)
```

