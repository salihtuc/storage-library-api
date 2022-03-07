# storage-library-api
A custom Python API which is using for storing a dictionary in a custom destination
<br>
The API supports JSON and XML storage formats and File System and Amazon S3 destinations.
Any storage format can be used with any destination.
<br>

For adding new storage format or destination, you can follow the guide in __For Developers__ section.

This repo also contains a sub-repo which is a simple Stack interface and its implementation (and tests) under 
__stack_interface__ folder in this repo.

## 1. Stack Interface

This repo contains two Python files:
* __stack_impl.py__
  * Simple Stack Interface and its implementation.
* __test_stack_impl.py__
  * Testing of the interface implementation with unittest.TestCase module.

### __stack_impl.py__
It contains following methods:
```
def size(self):
    """Returns an integer representing the total number of items in the stack."""

def push(self, element):
    """Pushes the element onto the top of the stack."""

def pop(self):
    """Removes the top element from the stack and returns its value."""

def peek(self):
    """Retrieves the top element from the stack without removing it, and returns its value."""

def empty(self):
    """Tests whether the stack is empty. Returns True if the stack is empty, False otherwise."""
```

The stack implementation holds the stack in a private Python list called elements.
<br>
As defaults in a Python list, the stack can contain any type of element in it.


Also, in addition to stack and its implementation, this code contains two custom `Exception` class
called `NullElementException` and `EmptyStackException`.

#### Technical Details

The interface `IStackInterface` is a subclass of Python's _ABC (Abstract Base Classes)_ module.

You can extend or implement this interface by inheriting this interface. <br>
Note that, you should implement all methods in this interface to inherit.


## 2. Storage Library API
### Usage
The `main.py` in this repository contains a demonstration of 
this library with JSON storage format and File System destination.

Simple usage:

```
# Create a sample dict
some_dict = {'a': 5, 'b': '4'}
    
# Create a sample record
record = Record('sample', some_dict)

# Call Custom destination and format
destination = FileDestination()
json_format = JsonFormat()

# Custom record operations
record.insert({"a": 55, "c": 14, "d": 'value'})

# Store the record
stored_file = destination.store(record, json_format)

print('{} stored in file system.'.format(stored_file))

# Get the record from stored file 
record_from_system = destination.parse(stored_file, json_format)
print('\nContent:')
print(record_from_system)
```

#### Detailed Explanation
All process can be separated into a few steps:

* **Preparing key/value data**
  * Create a `dict` which represents all the key/value pairs.
* **Preparing Record**
  * Create a `Record` object with the dict and a name.
    * Note that the name will be used as storage file name.
  * Insert/Update/Delete on the `Record` object.
* **Preparing storage format & destination**
  * Preparing Storage Format (Supported ones (for now): **_JSON_**, **_XML_**)
    * Just import the format from `formats`.
  * Preparing Destination Store (Supported ones (for now): **_File System_**, **_Amazon S3_**)
    * Just import the store from `destinations`.
* **Store/parse operation**
  * From the `destination` object, call the `store`/`parse` methods with appropriate format.

### For Developers
If you want to register/extend new storage format or destination for this library,
you can use information under this section.

#### Extending Storage Format
All the default storage formats are stored under `formats.py` file.

In this file, we have a base abstract class called `Destination`. <br>
For adding a new storage format, you should just create a **subclass** which inherits `Destination`.

Destination class has two functions that requires to implement: `to_format` and `from_format`.

`def to_format(self, attrs):`<br>
This function accepts a dictionary as input and converts it to 
string representation of desired format.

`def from_format(self, formatted: str):`<br>
This function accepts a formatted string of desired format as input 
and converts it to a dictionary object.



<h2>____ _TO BE CONTINUED_ ____<h2>
