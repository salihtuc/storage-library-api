import abc


class NullElementException(Exception):
    pass


class EmptyStackException(Exception):
    pass


class IStackInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'size') and
                callable(subclass.size) and
                hasattr(subclass, 'push') and
                callable(subclass.push) and
                hasattr(subclass, 'pop') and
                callable(subclass.pop) and
                hasattr(subclass, 'peek') and
                callable(subclass.peek) and
                hasattr(subclass, 'empty') and
                callable(subclass.empty)
                or
                NotImplemented)

    @abc.abstractmethod
    def size(self):
        """Returns an integer representing the total number of items in the stack."""
        raise NotImplementedError

    @abc.abstractmethod
    def push(self, element):
        """Pushes the element onto the top of the stack."""
        raise NotImplementedError

    @abc.abstractmethod
    def pop(self):
        """Removes the top element from the stack and returns its value."""
        raise NotImplementedError

    @abc.abstractmethod
    def peek(self):
        """Retrieves the top element from the stack without removing it, and returns its value."""
        raise NotImplementedError

    @abc.abstractmethod
    def empty(self):
        """Tests whether the stack is empty. Returns True if the stack is empty, False otherwise."""
        raise NotImplementedError


class Stack(IStackInterface):

    __elements: []

    def __init__(self):
        self.__elements = []

    def size(self):
        """Overrides IStackInterface.size()"""
        return len(self.__elements)

    def push(self, element):
        """Overrides IStackInterface.push()"""
        if element is None:
            raise NullElementException

        self.__elements.append(element)

    def pop(self):
        """Overrides IStackInterface.pop()"""
        if self.empty():
            raise EmptyStackException

        return self.__elements.pop()

    def peek(self):
        """Overrides IStackInterface.peek()"""
        if self.empty():
            raise EmptyStackException

        return self.__elements[-1]

    def empty(self):
        """Overrides IStackInterface.empty()"""
        return self.size() == 0
