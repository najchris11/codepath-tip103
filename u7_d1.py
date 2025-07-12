# def count_layers(sandwich):
#     if len(sandwich) == 1: return 1
#     else: return 1 + count_layers(sandwich[1])


# sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
# sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

# print(count_layers(sandwich1))
# print(count_layers(sandwich2))
    

# def revHelper(orders):
#     lst = orders.split()
#     if len(lst) == 1:
#         return orders
#     else: 
#         return lst[-1] + " " + revHelper(" ".join(lst[:-1]))

# print(revHelper("Bagel Sandwich Coffee"))

# def can_split_coffee(coffee, n):
#     vol = coffeeVol(coffee)
#     return vol % n == 0

# def coffeeVol(coffee):
#     if len(coffee) == 1:
#         return coffee[0]
#     else:
#         return coffee[0] + coffeeVol(coffee[1:])

# print(can_split_coffee([4, 4, 8], 2))
# print(can_split_coffee([5, 10, 15], 4))
# print(can_split_coffee([7, 3, 2], 2))
# print(can_split_coffee([1, 2, 3, 5, 5], 2))

# TODO: um what

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_orders(sandwich_a, sandwich_b)
    pass


sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))
