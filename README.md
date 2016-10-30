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
### Async methods

#### getting data from appbase 

```python

from asyncio import get_event_loop,gather
from pyappbase import Appbase

USERNAME="7eJWHfD4P"
PASSWORD="431d9cea-5219-4dfb-b798-f897f3a02665"
APPNAME="jsfiddle-demo"

  
  
appbaseRef = Appbase(USERNAME,PASSWORD,APPNAME)

loop = get_event_loop()
tasks = gather(appbaseRef.ping(), appbaseRef.get({"type":"Books","id":"X2"}))
print(loop.run_until_complete(tasks))

```

**Console Output**

```
[{"status":200,"message":"You have reached /jsfiddle-demo/ and are all set to make API requests"},
{'_index': 'jsfiddle-demo', '_version': 215, '_type': 'Books', 'found': True, '_id': 'X2', '_source': {'price': 5295, 'department_id': 1, 'department_name': 'Books', 'name': 'A Fake Book on Network Routing'}}
]
```

### getting streaming data from appbase

```

loop.run_until_complete(appbaseRef.get_stream({"type":"Books","id":"X2"},lambda resp : print(resp)))

```

**Console Output**
```
{
"_index":"jsfiddle-demo",
"_type":"Books",
"_id":"X2",
"_version":237,
"found":true,
"_source":{"department_name": "Books", "price": 5295, "department_id": 1, "name": "A Fake Book on Network Routing"}
}

```

This method will call the callback every time there is an update in the document with id `X2`

### stream searching the data from appbase

```
loop.run_until_complete(self.appbase.search_stream({"type":"Books","query": {"match_all":{}}},lambda word: print(word)))

```

**Console Output**

```
{
    "_shards": {
        "failed": 0,
        "successful": 1,
        "total": 1
    },
    "hits": {
        "hits": [
            {
                "_id": "AVXGXGx_GQ6uHvIS8e4h",
                "_index": "jsfiddle-demo",
                "_score": 1.0,
                "_source": {
                    "department_id": 1,
                    "department_name": "Books",
                    "name": "A Fake Book on Network Routing",
                    "price": 5595
                },
                "_type": "Books"
            },
            {
                "_id": "response",
                "_index": "jsfiddle-demo",
                "_score": 1.0,
                "_source": {
                    "department_id": 1,
                    "department_name": "Books",
                    "name": "A Fake Book on Network Routing",
                    "price": 5595
                },
                "_type": "Books"
            },
            {
                "_id": "11",
                "_index": "jsfiddle-demo",
                "_score": 1.0,
                "_source": {
                    "department_id": 1,
                    "department_name": "Books",
                    "name": "A Fake Book on Network Routing",
                    "price": 5596
                },
                "_type": "Books"
            },
            {
                "_id": "1",
                "_index": "jsfiddle-demo",
                "_score": 1.0,
                "_source": {
                    "department_id": 2,
                    "department_name": "Books",
                    "department_name_analyzed": "Books",
                    "name": "A Fake Book on Network Routing",
                    "price": 1952
                },
                "_type": "Books"
            },
            {
                "_id": "X1",
                "_index": "jsfiddle-demo",
                "_score": 1.0,
                "_source": {
                    "department_id": 1,
                    "department_name": "Books",
                    "name": "A Fake Book on Network Routing",
                    "price": 5595
                },
                "_type": "Books"
            },
            {
                "_id": "X3",
                "_index": "jsfiddle-demo",
                "_score": 1.0,
                "_source": {
                    "department_id": 1,
                    "department_name": "Books",
                    "name": "A Fake Book on Distributed Compute",
                    "price": 5295
                },
                "_type": "Books"
            },
            {
                "_id": "X2",
                "_index": "jsfiddle-demo",
                "_score": 1.0,
                "_source": {
                    "department_id": 1,
                    "department_name": "Books",
                    "name": "A Fake Book on Network Routing",
                    "price": 5295
                },
                "_type": "Books"
            }
        ],
        "max_score": 1.0,
        "total": 7
    },
    "timed_out": false,
    "took": 4
}
```

Similar to the `get_stream` method if any new record are added to the type `Books` then the callback will be executed in real time.





