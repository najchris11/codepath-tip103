# def words_with_char(words, x):
# 	retList = []
# 	for i, word in enumerate(words):
# 		if x in word:
# 			retList.append(i)
# 	return retList

# words = ["batman", "superman"]
# x = "a"
# print(words_with_char(words, x))

# words = ["black panther", "hulk", "black widow", "thor"]
# x = "a"
# print(words_with_char(words, x))

# words = ["star-lord", "gamora", "groot", "rocket"]
# x = "z"
# print(words_with_char(words, x))

# def hulk_smash(n):
#     retList = []
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             retList.append("HulkSmash")
#         elif i % 5 == 0:
#             retList.append("Smash")
#         elif i % 3 == 0:
#             retList.append("Hulk")
#         else:
#             retList.append(str(i))
#     return retList

# n = 3
# print(hulk_smash(n))

# n = 5
# print(hulk_smash(n))

# n = 15
# print(hulk_smash(n))


# def shuffle(message, indices):
# 	retList = []
# 	for num in indices:
# 		retList.append(message[num])
# 	return "".join(retList)

# message = "evil"
# indices = [3, 1, 2, 0]
# print(shuffle(message, indices))

# message = "findme"
# indices = [0, 1, 2, 3, 4, 5]
# print(shuffle(message, indices))


def minimum_boxes(meals, capacity):
	numMeals = sum(meals)
	sortedCap = sorted(capacity, True)
