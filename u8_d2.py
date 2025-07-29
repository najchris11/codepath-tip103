# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def right_vine(root):
#     if not root:
#         return []
    
#     def helper(root):
#         retList = [root.val]
#         if root.right:
#             return retList + helper(root.right)
#         return retList
    
#     return helper(root)

# """
#         Root
#       /      \
#     Node1    Node2
#   /         /    \
# Leaf1    Leaf2  Leaf3
# """
# ivy1 = TreeNode("Root", 
#                 TreeNode("Node1", TreeNode("Leaf1")),
#                 TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

# """
#       Root
#       /  
#     Node1
#     /
#   Leaf1  
# """
# ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def sum_inventory(inventory):
#     # if not inventory:
#     #     return 0
    
#     # def helper(node):
#     #     total = 0
#     #     if node.left:
#     #         total += helper(node.left)
#     #     if node.right:
#     #         total += helper(node.right)
#     #     total += node.val
#     #     return total
#     # return helper(inventory)

#     if not inventory:
#         return 0
    
#     return inventory.val + sum_inventory(inventory.left) + sum_inventory(inventory.right)


# """
#      40
#     /  \
#    5   10
#   /   /  \
# 20   1   30
# """

# inventory = TreeNode(40, 
#                     TreeNode(5, TreeNode(20)),
#                             TreeNode(10, TreeNode(1), TreeNode(30)))

# print(sum_inventory(inventory))


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def helper(root):
    if root.left:
        helper(root.left)
    if root.right:
        helper(root.right)
    # retList.append(root.val)

def helper(a, b, operator):
    if operator == '+':
        return a+b
    if operator == '-':
        return a-b
    if operator == '*':
        return a*b
    else:
        return a/b

def calculate_yield(root):
    if not root:
        return 0
    
    if root.val in ['+', '-', '*', '/']:
        return helper(calculate_yield(root.left), calculate_yield(root.right), root.val)
    
    return root.val


"""
      +
     / \ 
    /   \
   -     *
  / \   / \
 4   2 10  2
"""

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))
