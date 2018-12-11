class _DoublyLinkedBase:
    """ A base class providing a doubly linked list representation. """

    class _Node:
        """ Lightweight, nonpublic class for storing a doubly linked node. """
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """ Create an empty list. """
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        inserted = self._Node(e, predecessor, successor)
        predecessor._next = inserted
        successor._prev = inserted
        self._size += 1
        return inserted

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        element = node._element
        node._prev = node._next = node._element = None
        self._size -= 1
        return element


class PositionalList(_DoublyLinkedBase):
    """ A sequential container of elements allowing positional access. """

    #--------------------nested Position class----------------------------
    class Position:
        """ An abstraction representing the location of a single element. """
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """ Return the element stored at this Position. """
            return self._node._element

        def __eq__(self, other):
            """ Return True if other is a Position representing the same location. """
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """ Return True if other does not represent the same location. """
            return not(self == other)

    #---------------------utility methods----------------------------
    def _validate(self, p):
        """ Return position's node, or raise appropriate error if invalid. """
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """ Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    #--------------------accessors-------------------------------
    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """ Generate a forward iteration of the elements of the list. """
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #-----------------------------mutators-------------------------
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """ Insert element e at the front of the list and return new Position"""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)

    def add_after(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node, node._prev)

    def delete(self, p):
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, p, e):
        node = self._validate(p)
        temp = node._element
        node._element = e
        return temp


