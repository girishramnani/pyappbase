# pyappbase

[![Build Status](https://travis-ci.org/girishramnani/pyappbase.svg?branch=master)](https://travis-ci.org/girishramnani/pyappbase) [![Code Issues](https://www.quantifiedcode.com/api/v1/project/4b0e4fcebe10488b941d7c6719ad2f7c/badge.svg)](https://www.quantifiedcode.com/app/project/4b0e4fcebe10488b941d7c6719ad2f7c) [![Coverage Status](https://coveralls.io/repos/github/girishramnani/pyappbase/badge.svg?branch=master)](https://coveralls.io/github/girishramnani/pyappbase?branch=master)
<hr/>
python client for appbase

## how to 

```
python setup.py install
```
## Quick Start

The appbase object is the entry point for all methods, it supports both asynchronous and synchronous ways of communication. But its recommended to use async method if you will be using the streaming features of appbase. By default all the methods are asynchronous. you can change that by calling the `_set_async(False)` method on the appbase object.
 

#### getting data from appbase ( sync method ) 

```python

from pyappbase import Appbase

USERNAME="7eJWHfD4P"
PASSWORD="431d9cea-5219-4dfb-b798-f897f3a02665"
APPNAME="jsfiddle-demo"

  
  
appbaseRef = Appbase(USERNAME,PASSWORD,APPNAME)
appbaseRef._set_async(False)
print(appbaseRef.get({
            "type": "Books",
            "id": "X2",
        }))


```

**Console Output**

```
{'_index': 'jsfiddle-demo',
'found': True, 
'_source': {'price': 5295, 'department_id': 1, 'department_name': 'Books', 'name': 'A Fake Book on Network Routing'},
'_id': 'X2', 
'_type': 'Books',
'_version': 177
}
```

#### indexing data into appbase ( sync method )

we will be using the same `appbaseRef` object from above

```python

print(appbaseRef.index({
            "type": "Books",
            "id": "X4",
            "body": {
                "department_id": 2,
                "department_name": "Books",
                "name": "A Fake Book on Algorithms",
                "price": 5295
            }
        }))

```

**Console Output**

```
{'_index': 'jsfiddle-demo',
'created': False,
'_type': 'Books', 
'_version': 3,
'_id': 'X4',
'_shards': {'failed': 0, 'successful': 2, 'total': 2}
}
```
This means the document was stored successfully.

#### deleting the data from appbase ( sync method )

```python

print(appbaseRef.delete({"type":"Books","id":"X4"}))

```

**Console Output**

```
{'found': True, 
'_shards': {'total': 2, 'successful': 2, 'failed': 0}, 
'_version': 5, 
'_type': 'Books',
'_id': 'X4',
'_index': 'jsfiddle-demo'}
```



