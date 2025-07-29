from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)



# class Puff():
#      def __init__(self, flavor, left=None, right=None):
#         self.val = flavor
#         self.left = left
#         self.right = right

# def listify_design(design):
#     # U - BST output is a list of lists of ever element on a queue
#     # P - bfs and add to a list

#     if not design:
#         return []
    
#     queue = deque()
#     retList = []
#     queue.append(design)
#     while queue:
#         visited = []
#         for _ in range(len(queue)):
#             ptr = queue.popleft()
#             visited.append(ptr.val)
#             if ptr.left:
#                 queue.append(ptr.left)
#             if ptr.right:
#                 queue.append(ptr.right)
#         retList.append(visited)
    

#     return retList


# """
#             Vanilla
#            /       \
#       Chocolate   Strawberry
#       /     \
#   Vanilla   Matcha  
# """
# croquembouche = Puff("Vanilla", 
#                     Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
#                     Puff("Strawberry"))
# print(listify_design(croquembouche))


# class TreeNode():
#      def __init__(self, flavor, left=None, right=None):
#         self.val = flavor
#         self.left = left
#         self.right = right

# def zigzag_icing_order(cupcakes):
#     if not cupcakes:
#         return []
    
#     queue = deque()
#     retList = []
#     queue.append(cupcakes)
#     reverse = False
#     while queue:
#         level = deque()
#         for _ in range(len(queue)):
#             ptr = queue.popleft()
#             if reverse:
#                 level.appendleft(ptr.val)
#             else:
#                 level.append(ptr.val)
#             if ptr.left:
#                 queue.append(ptr.left)
#             if ptr.right:
#                 queue.append(ptr.right)
#         retList.extend(level)   
#         reverse = not reverse 

#     return list(retList)


# """
#             Chocolate
#            /         \
#         Vanilla       Lemon
#        /              /    \
#     Strawberry   Hazelnut   Red Velvet   
# """

# # Using build_tree() function included at top of page
# flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
# cupcakes = build_tree(flavors)
# print(zigzag_icing_order(cupcakes))

class TreeNode():
     def __init__(self, order_size, left=None, right=None):
        self.val = order_size
        self.left = left
        self.right = right

def larger_order_tree(orders):
    def dfs(node, sum):
        rightSum = dfs(node.right)
        node.val += rightSum
        dfs(node.left)



"""
         4
       /   \
      /     \
     1       6
    / \     / \
   0   2   5   7
        \       \
         3       8   
"""
# using build_tree() function included at top of page
order_sizes = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
orders = build_tree(order_sizes)

# using print_tree() function included at top of page
print_tree(larger_order_tree(orders))
