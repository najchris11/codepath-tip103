from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

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

# class Puff():
#      def __init__(self, flavor, left=None, right=None):
#         self.val = flavor
#         self.left = left
#         self.right = right
# # U - taking in a bst and returning list of list
# # add one level's contents to the total list
# # M - so take the 
# def listify_design(design):
#     if not design: 
#         return []
#     result = []
#     queue = deque()
#     queue.append(design)
#     while queue:
#         level = []
#         size = len(queue)
#         for _ in range(size):
#             node = queue.popleft()
#             level.append(node.val)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         result.append(level)
#     return result
    
    

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
#     result = []
#     queue = deque()
#     queue.append(cupcakes)
#     reverse = False
#     while queue:
#         size = len(queue)
#         level = []
#         for _ in range(size):
#             if not reverse:
#                 node = queue.popleft()
#                 level.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             else:
#                 node = queue.pop()
#                 level.append(node.val)
#                 if node.right:
#                     queue.appendleft(node.right)
#                 if node.left:
#                     queue.appendleft(node.left)
#         result.extend(level)
#         reverse = not reverse
#     return result


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

# class TreeNode():
#      def __init__(self, order_size, left=None, right=None):
#         self.val = order_size
#         self.left = left
#         self.right = right

# def larger_order_tree(orders):
#     total = 0
#     def reverseInOrder(node):
#         nonlocal total
#         if not node:
#             return
#         reverseInOrder(node.right)
#         total += node.val
#         node.val = total
#         reverseInOrder(node.left)
#     reverseInOrder(orders)
#     return orders

# """
#          4
#        /   \
#       /     \
#      1       6
#     / \     / \
#    0   2   5   7
#         \       \
#          3       8   
# """
# # using build_tree() function included at top of page
# order_sizes = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
# orders = build_tree(order_sizes)

# # using print_tree() function included at top of page
# print_tree(larger_order_tree(orders))


class TreeNode():
     def __init__(self, order, left=None, right=None):
        self.val = order
        self.left = left
        self.right = right

def larger_order_tree(order_tree, order):
    if not order_tree: 
        return None
    queue = deque()
    queue.append(order_tree)
    while queue:
        level = []
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if order in level:
            if level.index(order) == len(level): return None
            else: return level[level.index(order) + 1]
    return None


"""
        Cupcakes
       /       \ 
   Macaron     Cookies      
        \      /      \
      Cake   Eclair   Croissant
"""
cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = larger_order_tree(cupcakes, cake)
next_order2 = larger_order_tree(cupcakes, cookies)
print(next_order1.val)
print(next_order2.val)
