# MicroDB
Smallest Python Database Possible

## Usage

Initiate a new MicroDB instance.
```python
from microdb import D as MicroDB

db = MicroDB()
```

Save data into the database.
```python
db.key = 'value'
```

Retrieve data from the database.
```python
db.key
>>> 'value'
```

Load data from the database.
```python
from microdb import D as MicroDB

db = MicroDB()
db.l()

db.key
>>> 'value'
```
