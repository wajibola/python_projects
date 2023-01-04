"""
@author: waziri
"""

# Consider the implementation of a Tree class that implements non-empty trees:
# Also, define a subclass of class Tree called PreTree, adding the method preorder that returns a
# list with the elements of the tree ordered.

class Tree: 
    def __init__(self, x):
        self.rt = x
        self.child = []
    
    def add_child(self, a): 
        self.child.append(a)
    
    def root(self): 
        return self.rt
    
    def ith_child(self, child_id):
        # returns child i of the tree (counting from zero).
        return self.child[child_id] if (len(self.child)-1 >= child_id) else None
            
    def num_children(self):
        # returns number of childs of the tree.
        return len(self.child)
    

class PreTree(Tree):
    def __init__(self, x):
        super(PreTree, self).__init__(x)
    
    def preorder(self):
        # returns a list with the elements of the tree ordered.
        return sorted(self._recursive_check())

    def _recursive_check(self):
        for child in self.child:
            yield from child._recursive_check()
        yield self.rt


t = PreTree(2)
t.add_child(PreTree(3))
t.add_child(PreTree(5))
n_children = t.num_children()
print(f"Number of children is: {n_children}")
t.ith_child(1).add_child(PreTree(4))
print(t.preorder())
