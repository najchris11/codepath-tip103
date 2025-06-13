from collections import deque

# def arrange_guest_arrival_order(arrival_pattern):
#   guest_order = ""
#   stack = []

#   for i, guest in enumerate(arrival_pattern):
#     if guest == "I":
#       guest_order += str(i+1)
#     else:
#       stack.append(str(i+1))
#       index = i
#       while index < len(arrival_pattern):
#         if arrival_pattern[index] == "I":
#             guest_order += str(index)
#             i = index + 1
#             break
#         index += 1
#     stack.append(str(i+1))
#     while stack:
#       guest_order += stack.pop()
#     return guest_order
  
# print(arrange_guest_arrival_order("IIIDIDDD"))  
# print(arrange_guest_arrival_order("DDD"))  

def reveal_attendee_list_in_order(attendees):
  q = deque()
  
