import json


class Node:

    def __init__(self, name):
        self.name = name
        self._parent = None
        self._children = set()
        self.value = None

    def __repr__(self):
        return f'{self.id} = {self.value}'

    def __iter__(self):
        yield self
        for child in self.children:
            yield from child

    def __len__(self):
        counter = 0
        for _ in self:
            counter += 1
        return counter

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
        if self.parent is None:
            return self.name
        return f'{self.parent.id}{sep}{self.name}'


    @classmethod
    def parse(cls, config):
        """
        Recursively parse a dictionary to create a tree

        :param dict config: Dictionary to parse into Nodes
        :return Iterable[Node]: Iterable of newly created Nodes
        """
        nodes = set()

        for k, v in config.items():
            # Create node object
            node = cls(k)
            # Add current node to set of nodes parsed at this level
            nodes.add(node)
            # Ignore children if null value found
            if v is None:
                continue
            # Add any children nodes recursively
            children = cls.parse(v)
            for child in children:
                node.add_child(child)

        return nodes

    @classmethod
    def load(cls, file):
        """
        Load a JSON file into a tree object
        * Assume top level has only one key (root) *

        :param str file: JSON tree file path
        :return Node: Root Node of tree created from file
        """
        with open(file, 'r') as r:
            config = json.load(r)
        return cls.parse(config).pop()

    def add_child(self, node):
        """
        Add a child node

        :param Node node: Child to add
        """
        self.children.add(node)
        node._parent = self

    def get(self, path, sep='.'):
        """
        Get a node by ID

        :param str path: Relative path to node
        :param str sep: Separator char
        :return Node: Node at path, or raise KeyError if not found
        """

        name, *remaining = path.split(sep)
        for child in self._children:
            if child.name != name:
                continue

            if remaining:
                return child.get(sep.join(remaining), sep=sep)
            return child

        raise KeyError

    def update(self, payload):
        """
		Update node values in the tree by ID

        :param dict payload: Dictionary tree ID / value pairs
        """
        for k, v in payload.items():
            try:
                node = self.get(k)
            except KeyError:
                pass
            else:
                node.value = v


#########
# TESTS #
#########

tree = Node.load('tree.json')

assert len(tree) == 21

payload = {
    'rack1.sg1': 10,
    'rack1.sg1.cmp1': 5,
    'rack1.sg1.ckt1.case2': 20,
    'rack1.sg2.ckt1': 30,
    'rack2.sg1.ckt1.case1': 20, 
    'rack2.sg1.ckt1.case5': 20,  # Does not exist
}
tree.update(payload)

assert tree.get('rack1.sg1').value == 10
assert tree.get('rack1.sg1.cmp1').value == 5
assert tree.get('rack2.sg1.ckt1.case1').value == 20
assert tree.get('rack1.sg1.cmp2').value == None
try:
	tree.get('rack2.sg1.ckt1.case5')
	assert False
except KeyError:
	assert True


