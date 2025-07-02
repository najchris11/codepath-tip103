# class Villager:
#     def __init__(self, name, species, personality, catchphrase, neighbor = None):
#         self.name = name
#         self.species = species
#         self.personality = personality
#         self.catchphrase = catchphrase
#         self.furniture = []
#         self.neighbor = neighbor


#     def add_item(self, item_name):
#         arr = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
#         if item_name in arr:
#             self.furniture.append(item_name)

# def of_personality_type(townies, personality_type):
#     retList = []
#     for villager in townies:
#         if villager.personality == personality_type:
#             retList.append(villager.name)
#     return retList


# # apollo = Villager("Apollo", "Eagle", "pah")
# # print(apollo.name)
# # print(apollo.species) 
# # print(apollo.catchphrase)
# # print(apollo.furniture)

# # isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# # bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# # stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# # print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# # print(of_personality_type([isabelle, bob, stitches], "Cranky"))

# def message_received(start_villager, target_villager):
#     neighbor = start_villager.neighbor
#     while neighbor and neighbor != target_villager:
#         neighbor = neighbor.neighbor
#     if neighbor: return True
#     return False

# # isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# # tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
# # kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
# # isabelle.neighbor = tom_nook
# # tom_nook.neighbor = kk_slider

# # print(message_received(isabelle, kk_slider))
# # print(message_received(kk_slider, isabelle))

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

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

# print_linked_list(kk_slider)
def catch_fish(head):
    if head:
        print(f"I caught a {head.value}")
        head = head.next
    else:
        print("Aw! Better luck next time!")
    return head


fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

# print_linked_list(fish_list)
# print_linked_list(catch_fish(fish_list))
# print(catch_fish(empty_list))


def fish_chances(head, fish_name):
    fishOcc, numOfFish = 0, 0
    fish = head
    while fish:
        numOfFish += 1
        if fish.value == fish_name:
            fishOcc += 1
        fish = fish.next
    return round(fishOcc/numOfFish, 2)

# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print(fish_chances(fish_list, "Dace"))
# print(fish_chances(fish_list, "Rainbow Trout"))

def restock(head, new_fish):
    ptr = head
    while ptr.next:
        ptr = ptr.next
    fish = Node(new_fish)
    ptr.next = fish
    return head



# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print_linked_list(restock(fish_list, "Rainbow Trout"))

def has_cycle(head):
    if not head: return False
    slow, fast = head, head.next
    while slow and fast:
        if slow == fast:
            return True
        slow = slow.next
        # add exception handling to exit loop
        fast = fast.next.next
    return False

peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# Toad.next = Luigi
peach.next.next.next = peach.next

print(has_cycle(peach))
# Test Case 1: Empty list
print("Test 1:", has_cycle(None))  # False

# Test Case 2: Single node, no cycle
a = Node("A")
print("Test 2:", has_cycle(a))  # False

# Test Case 3: Two nodes, no cycle
a = Node("A")
b = Node("B")
a.next = b
print("Test 3:", has_cycle(a))  # False

# Test Case 4: Two nodes, cycle (B points back to A)
a = Node("A")
b = Node("B")
a.next = b
b.next = a
print("Test 4:", has_cycle(a))  # True

# Test Case 5: Longer list, no cycle
a = Node("A", Node("B", Node("C", Node("D"))))
print("Test 5:", has_cycle(a))  # False

# Test Case 6: Longer list, cycle at the end (D -> B)
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
a.next = b
b.next = c
c.next = d
d.next = b
print("Test 6:", has_cycle(a))  # True

# Test Case 7: Cycle includes entire list (A -> A)
a = Node("A")
a.next = a
print("Test 7:", has_cycle(a))  # True