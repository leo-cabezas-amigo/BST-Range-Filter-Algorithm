# -*- coding: utf-8 -*-

# FILE NAME: performance_comparison.py
# AUTHOR: Leo Cabezas Amigo (NIA: 100504261)

from bintree import BinaryNode
from bst import BinarySearchTree

class BSTa(BinarySearchTree):   # Class for my solution
    def __init__(self):
        super(BSTa, self).__init__()
        self.recursions = 0 # Recursion call count

    def outsideRange(self, min: int, max: int) -> list:
        list1 = []
        list2 = []
        
        self._outsideRangeFromBelow(min, self._root, list1)
        self._outsideRangeFromAbove(max, self._root, list2)
        
        return list1 + list2

    def _outsideRangeFromBelow(self, min: int, node: BinaryNode, myList: list):
        self.recursions += 1    # Updates recursion call count
        
        if node == None:
            return
        if node.left == None and node.right == None and node.elem < min:
            myList.append(node.elem)
        
        # MODIFICATION: empty nodes are not visited, thus increasing performance
        if node.elem >= min:
            if node.left != None: self._outsideRangeFromBelow(min, node.left, myList)
        else:
            if node.left != None: self._outsideRangeFromBelow(min, node.left, myList)
            if node.right != None: self._outsideRangeFromBelow(min, node.right, myList)

    def _outsideRangeFromAbove(self, max: int, node: BinaryNode, myList: list):
        self.recursions += 1    # Updates recursion call count
    
        if node == None:
            return
        if node.left == None and node.right == None and node.elem > max:
            myList.append(node.elem)
        
        # MODIFICATION: empty nodes are not visited, thus increasing performance
        if node.elem <= max:
            if node.right != None: self._outsideRangeFromAbove(max, node.right, myList)
        else:
            if node.left != None: self._outsideRangeFromAbove(max, node.left, myList)
            if node.right != None: self._outsideRangeFromAbove(max, node.right, myList)

class BSTb(BinarySearchTree):   # Class for your solution (identical to class BSTb in solution_classes_no_mod.py)
    def __init__(self):
        super(BSTb, self).__init__()
        self.recursions = 0 # Recursion call count

    def outsideRange(self, min: int, max: int) -> list:
        leafs = []
        self._outsideRange(self._root, min, max, leafs)
        return leafs

    # finds all nodes having value outside the given range
    def _outsideRange(self, node: BinaryNode, min: int, max: int, leafs: []) -> object:
        self.recursions += 1    # Updates recursion call count
        if node is not None:
            node.left = self._outsideRange(node.left, min, max, leafs)
            if (node.left is None) and (node.right is None) and (node.elem < min or node.elem > max):
                # node is a leave, append node in list
                leafs.append(node.elem)
            node.right = self._outsideRange(node.right, min, max, leafs)

        # if node is not leaf, return node and continue recursion
        return node

