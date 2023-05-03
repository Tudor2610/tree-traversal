import unittest

from tree import Tree

class treeTest(unittest.TestCase):

    def test_find(self):
        tree = Tree()
        tree.add(5)
        tree.add(3)
        tree.add(2)
        tree.add(4)
        tree.add(7)
        tree.add(6)
        tree.add(8)
        self.assertEqual(tree.find(5).data, 5)
        self.assertEqual(tree.find(3).data, 3)
        self.assertEqual(tree.find(2).data, 2)
        self.assertEqual(tree.find(4).data, 4)
        self.assertEqual(tree.find(7).data, 7)
        self.assertEqual(tree.find(6).data, 6)
        self.assertEqual(tree.find(8).data, 8)

    def test_find_not_in_tree(self):
        tree = Tree()
        tree.add(5)
        tree.add(3)
        tree.add(2)
        tree.add(4)
        tree.add(7)
        tree.add(6)
        tree.add(8)
        self.assertEqual(tree.find(9), None)


if __name__ == '__main__':
    unittest.main()
