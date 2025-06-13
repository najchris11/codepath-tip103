from collections import deque
# def arrange_guest_arrival_order(arrival_pattern):
#   arrival_pattern += "I"
#   guest_order = ""
#   lower_priority = deque()
#   for index, guest in enumerate(arrival_pattern):
#     adjIndex = index + 1
#     if guest == 'I':
#       guest_order += str(adjIndex)
#       while lower_priority:
#         guest_order += str(lower_priority.pop())
#     elif guest == 'D':
#       lower_priority.append(str(adjIndex))
#   while lower_priority:
#     guest_order += str(lower_priority.pop())
#   return guest_order
      
# print(arrange_guest_arrival_order("IIIDIDDD"))  
# print(arrange_guest_arrival_order("DDD"))  


def reveal_attendee_list_in_order(attendees):
    ptr = 0
    retList = []
    sortedAttendees = deque(sorted(attendees))
    while ptr < len(sortedAttendees):
        sortedAttendees.append(sortedAttendees.popleft())
        retList.append(sortedAttendees.popleft())
        ptr += 1

    return retList
print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000]))  



# 2 3 5 7 11 13 17

# 2 3 5 7 -- 11 13 -- 17

# 2 13 -- 3 11 -- 5 17 -- 7