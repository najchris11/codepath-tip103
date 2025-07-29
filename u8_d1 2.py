# # Problem 1: Ivy Cutting
# # You have a trailing ivy plant represented by a binary tree. 
# # You want to take a cutting to start a new plant using the rightmost vine in the plant. 
# # Given the root of the plant, 
# # return a list with the value of each node in the path from the root node to the rightmost leaf node.

# # Evaluate the time and space complexity of your function. 
# # Define your variables and provide a rationale for why you 
# # believe your solution has the stated time and space complexity. 
# # Assume the input tree is balanced when calculating time and space complexity.

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def right_vine(root):
#     '''
#     U - give the path to the rightmost node, and don't care abt left nodes in interior nodes in path
#     P - grab the root, while loop that follows the right child (until not None), and print node
#     '''
#     if not root:
#         return []
#     retList = [root.val]
#     ptr = root.right
#     while ptr:
#         retList.append(ptr.val)
#         ptr = ptr.right

#     return retList
  
# # Example Usage:

# # """
# #         Root
# #       /      \
# #     Node1    Node2
# #   /         /    \
# # Leaf1    Leaf2  Leaf3
# # """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# # """
# #       Root
# #       /  
# #     Node1
# #     /
# #   Leaf1  
# # """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# # print(right_vine(ivy1))
# # print(right_vine(ivy2))
# # Example Output:

# # ['Root', 'Node2', 'Leaf3']
# # ['Root']

# =========================
# Problem 2: Ivy Cutting2
# You have a trailing ivy plant represented by a binary tree. 
# You want to take a cutting to start a new plant using the rightmost vine in the plant. 
# Given the root of the plant, 
# return a list with the value of each node in the path from the root node to the rightmost leaf node.

# Evaluate the time and space complexity of your function. 
# Define your variables and provide a rationale for why you 
# believe your solution has the stated time and space complexity. 
# Assume the input tree is balanced when calculating time and space complexity.

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def right_vine(root):
#     '''
#     U - give the path to the rightmost node, and don't care abt left nodes in interior nodes in path
#     P - grab the root, while loop that follows the right child (until not None), and print node
#     '''
#     if not root:
#         return []
        
#     def helper(root):
#         retList = [root.val]
#         if root.right:
#             return retList + helper(root.right)
#         return retList

#     return helper(root)

  
# # Example Usage:

# # """
# #         Root
# #       /      \
# #     Node1    Node2
# #   /         /    \
# # Leaf1    Leaf2  Leaf3
# # """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# # """
# #       Root
# #       /  
# #     Node1
# #     /
# #   Leaf1  
# # """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))
# # Example Output:

# # ['Root', 'Node2', 'Leaf3']
# # ['Root']


# =====================================
# Problem 3: Pruning Plans
# You have a large overgrown Magnolia tree that's in desperate 
# need of some pruning. Before you can prune the tree, 
# you need to do a full survey of the tree to evaluate which sections need to be pruned.

# Given the root of a binary tree representing the magnolia, 
# return a list of the values of each node using a postorder traversal. 
# In a postorder traversal, you explore the left subtree first, then the right subtree, 
# and finally the root. Postorder traversals are often used when deleting nodes from a tree.

# Evaluate the time and space complexity of your function. Define your variables and 
# provide a rationale for why you believe your solution has the stated time and space 
# complexity. Assume the input tree is balanced when calculating time and space complexity.

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# """
# U - do a postorder traversal on a tree and save its nodes in a list to be returned
# P - while current node, recursive call to traversal on left, and then right child, and then add the value to list
# """
# def survey_tree(root):
#     if not root:
#         return []

#     retList = []
#     def helper(root):
#         if root.left:
#             helper(root.left)
#         if root.right:
#             helper(root.right)
#         retList.append(root.val)

#     helper(root)
#     return retList


# # Example Usage:

# # """
# #         Root
# #       /      \
# #     Node1    Node2
# #   /         /    \
# # Leaf1    Leaf2  Leaf3
# # """

# magnolia = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                         TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# print(survey_tree(magnolia))
# # Example Output:

# # ['Leaf1', 'Node1', 'Leaf2', 'Leaf3', 'Node2', 'Root']


# ===============================
# Problem 4: Sum Inventory
# A local flower shop stores its inventory in a binary tree, where each node represents their current stock of a flower variety. Given the root of a binary tree inventory, return the sum of all the flower stock in the store.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# """
# U - Add all the values in a binary tree and return the total
# P - recursively call the function on each node and return its value, add all the values
# together in the end
# """
# def sum_inventory(inventory):
#     if not inventory:
#         return 0

#     return inventory.val + sum_inventory(inventory.left) + sum_inventory(inventory.right)

# # Example Usage:

# # """
# #      40
# #     /  \
# #    5   10
# #   /   /  \
# # 20   1   30
# # """

# inventory = TreeNode(40, 
#                     TreeNode(5, TreeNode(20)),
#                             TreeNode(10, TreeNode(1), TreeNode(30)))

# print(sum_inventory(inventory))
# # Example Output:

# # 106

# ======================================

# Problem 5: Calculating Yield II
# You have a fruit tree represented as a binary tree. Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

# Leaf nodes have an integer value.
# Non-leaf nodes have a string value of either "+", "-", "*", or "-".
# The yield of a the tree is calculated as follows:

# If the node is a leaf node, the yield is the value of the node.
# Otherwise evaluate the node's two children and apply the mathematical operation of its value with the children's evaluations.
# Return the result of evaluating the root node.

# Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right
# '''
# U - calculate the yield using the values from children and operators from interior nodes
# P - 

# def helper(root):
#          if root.left:
#              helper(root.left)
#          if root.right:
#              helper(root.right)
#          retList.append(root.val)
# '''

# def helper(a, b, operator):
#     if operator == '+':
#         return a + b
#     elif operator == '-':
#         return a - b
#     elif operator == '/':
#         return a / b
#     else:
#         return a * b

# def calculate_yield(root):
#     if not root:
#         return 0
        
#     if root.val in ['+', '-', '*', '/']:
#         return helper(calculate_yield(root.left), 
#                       calculate_yield(root.right),
#                       root.val)
    
#     return root.val
    

# # Example Usage:

# # """
# #       +
# #      / \ 
# #     /   \
# #    -     *
# #   / \   / \
# #  4   2 10  2
# # """

# root = TreeNode("+")
# root.left = TreeNode("-")
# root.right = TreeNode("*")
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(2)
# root.right.left = TreeNode(10)
# root.right.right = TreeNode(2)

# print(calculate_yield(root))
# # Example Output:

# # 22
# # Explanation:
# # - 4 - 2 = 2
# # - 10 * 2 = 20
# # - 2 + 20 = 22

# # Problem 6: Plant Classifications
# # Given the root of a binary tree used to classify plants where each level of the tree represents a higher degree of speficity, return an array with the most specific plant classification categories (aka the leaf node values). Leaf nodes are nodes with no children.

# # Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# """
# U - return a list of all the leaf nodes
# P - check each node recursively and add it to the list if it has no children -> leaf
# """
# def get_most_specific(taxonomy):
#     if not taxonomy:
#         return []
    
#     retList = []
#     def helper(taxonomy):
#         if not taxonomy.left and not taxonomy.right:
#             retList.append(taxonomy.val)
#         if taxonomy.left:
#             helper(taxonomy.left)
#         if taxonomy.right:
#             helper(taxonomy.right)

#     helper(taxonomy)

#     return retList
    
    
# # Example Usage:

# # """
# #            Plantae
# #           /       \
# #          /         \
# #         /           \ 
# # Non-flowering     Flowering
# #    /      \       /        \
# # Mosses   Ferns Gymnosperms Angiosperms
# #                              /     \
# #                         Monocots  Dicots
# # """
# plant_taxonomy = TreeNode("Plantae", 
#                           TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
#                                   TreeNode("Flowering", TreeNode("Gymnosperms"), 
#                                           TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots"))))

# print(get_most_specific(plant_taxonomy))
# # Example Output:

# # ['Mosses', 'Ferns', 'Gymnosperms', 'Monocots', 'Dicots']


# ===============================================
# # Problem 7: Count Old Growth Trees
# # Given the root of a binary tree where each node represents the age of a tree in a forest, write a function count_old_growth() that returns the number of old growth trees in the forest. A tree is considered old growth if it has age greater than threshold.

# # Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# """
# U - return 
# """
# def count_old_growth(root, threshold):
#     pass

# # Example Usage:

# # """
# #      100
# #      /  \
# #     /    \
# #   1200  1500
# #   /     /  \
# # 20    700  2600
# # """

# forest = TreeNode(100, 
#                   TreeNode(1200, TreeNode(20))
#                           TreeNode(1500, TreeNode(700), TreeNode(2600)))

# print(count_old_growth(forest, 1000))
# # Example Output:

# # 3

# 
"""
# Example 1

# Input: root = CoralKing
# Expected Output: True

# Example 2

    CoralQueen
     /      \
 CoralX    CoralX
  /  \      /  \
CoralY CoralZ CoralY CoralZ

# Input: root = CoralQueen
# Expected Output: False
"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

    """
    U - return true or false if these are both the left and right subtrees of the root are mirrors of each other
    P - make a helper for sub node, that will check if both nodes exist, and if they do, if they're equal
    call this helper recursively on 
    """

def is_symmetric(root):
    if not root:
        return True
    
    def helper(root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        return root1.val == root2.val and helper(root1.left, root2.right) and helper(root1.right, root2.left)
        
    return helper(root.left, root.right)
    
    
    

"""
        A
      /   \
     B     B
    / \   / \
   C  D   D  C
"""
coral1 = TreeNode('A', 
                  TreeNode('B', TreeNode('C'), TreeNode('D')), 
                          TreeNode('B', TreeNode('D'), TreeNode('C')))


"""
        A
      /   \
     B     B
    / \   / \
   C  D   C  D
"""
coral2 = TreeNode('A', 
                  TreeNode('B', TreeNode('C'), TreeNode('D')), 
                          TreeNode('B', TreeNode('C'), TreeNode('D')))

print(is_symmetric(coral1))
print(is_symmetric(coral2))