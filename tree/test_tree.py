import unittest

from tree import Node


class TestTree(unittest.TestCase):
    def setup(self):
        self.tree = Node.load('tree.json')

    def test_tree_loads_from_config(self):
        self.assertEqual(len(self.tree), 21)

    def test_tree_update(self):
        payload = {
            'rack1.sg1': 10,
            'rack1.sg1.cmp1': 5,
            'rack1.sg1.ckt1.case2': 20,
            'rack1.sg2.ckt1': 30,
            'rack2.sg1.ckt1.case1': 20,
            'rack2.sg1.ckt1.case5': 20,  # Does not exist
        }
        self.tree.update(payload)

        self.assertEqual(self.tree.get('rack1.sg1').value, 10)
        self.assertEqual(self.tree.get('rack1.sg1.cmp1').value, 5)
        self.assertEqual(self.tree.get('rack2.sg1.ckt1.case1').value, 20)
        self.assertIsNone(self.tree.get('rack1.sg1.cmp2').value)
        with self.assertRaises(KeyError):
            self.tree.get('rack2.sg1.ckt1.case5')


if __name__ == '__main__':
    unittest.main()
