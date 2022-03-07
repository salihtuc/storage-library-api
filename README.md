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

# Call Custom destination
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

<h2>____ _TO BE CONTINUED_ ____<h2>
