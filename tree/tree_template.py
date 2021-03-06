class Node:

    def __init__(self, name):
        self.name = name
        self._parent = None
        self._children = NotImplemented  # TODO: Choose iterable data structure
        self.value = None

    def __repr__(self):
        return f'{self.id} = {self.value}'

    def __iter__(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children

    @property
    def id(self, sep='.'):
        """
        Path of this Node from the root

        :param str sep: Separator char
        :return str: Path to Node from relative Node self
        """
        raise NotImplementedError

    @classmethod
    def parse(cls, config):
        """
        Recursively parse a dictionary to create a tree

        :param dict config: Dictionary to parse into Nodes
        :return Iterable[Node]: Iterable of newly created Nodes
        """
        raise NotImplementedError

    def add_child(self, node):
        """
        Add a child node

        :param Node node: Child to add
        """
        raise NotImplementedError

    @classmethod
    def load(cls, file):
        """
        Load a JSON file into a tree object
        * Assume top level has only one key (root) *

        :param str file: JSON tree file path
        :return Node: Root Node of tree created from file
        """
        raise NotImplementedError

    def get(self, path, sep='.'):
        """
        Get a node by ID

        :param str path: Relative path to node
        :param str sep: Separator char
        :return Node: Node at path, or raise KeyError if not found
        """
        raise NotImplementedError

    def update(self, payload):
        """
        Update node values in the tree by ID

        :param dict payload: Dictionary tree ID / value pairs
        """
        raise NotImplementedError
