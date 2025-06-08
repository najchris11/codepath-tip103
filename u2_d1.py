# def total_treasures(treasure_map):
#     totalValues = 0
#     for k,v in treasure_map.items():
#         totalValues += v
#     return totalValues

# treasure_map1 = {
#     "Cove": 3,
#     "Beach": 7,
#     "Forest": 5
# }

# treasure_map2 = {
#     "Shipwreck": 10,
#     "Cave": 20,
#     "Lagoon": 15,
#     "Island Peak": 5
# }

# print(total_treasures(treasure_map1)) 
# print(total_treasures(treasure_map2)) 

# def can_trust_message(message):
#     letterSet = set()
#     for c in message:
#         if c.isalpha():
#             letterSet.add(c.lower)
#     return len(letterSet) == 26

# message1 = "sphinx of black quartz judge my vowsphinx of black quartz judge my vow"
# message2 = "trust me"

# print(can_trust_message(message1))
# print(can_trust_message(message2))

# def find_duplicate_chests(chests):
#     firstTime, secondTime = [], []
#     for num in chests:
#         if num in firstTime:
#             firstTime.remove(num)
#             secondTime.append(num)
#         else:
#             firstTime.append(num)
#     return secondTime

# chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
# chests2 = [1, 1, 2]
# chests3 = [1]

# print(find_duplicate_chests(chests1))
# print(find_duplicate_chests(chests2))
# print(find_duplicate_chests(chests3))

def is_balanced(code):
    frqMap = {}
    for c in code:
        if c in frqMap:
            frqMap[c] += 1
        else:
            frqMap[c] = 1
    letterRemoved = False
    valArray = sorted(frqMap.values(), reverse=True)
    setVal = min(valArray[0], valArray[1])
    for v in valArray:
        if v != setVal:
            letterRemoved = True
        if not letterRemoved and v != setVal:
            return False
    
    return letterRemoved




code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 
print(is_balanced("aabbcc"))      # True
print(is_balanced("aabbccc"))     # True (remove one 'c')
print(is_balanced("aabbcccc"))    # False
print(is_balanced("aaa"))         # True
print(is_balanced("aaabbb"))      # False